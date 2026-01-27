from appwrite.client import Client
from appwrite.services.tables_db import TablesDB
from appwrite.query import Query
import os
from dotenv import load_dotenv
import json

load_dotenv()

databaseId = os.getenv('APPWRITE_DATABASE_ID')
loggedClimbsTable = os.getenv('APPWRITE_LOGGED_CLIMBS_TABLE')
climbsTable = os.getenv('APPWRITE_CLIMBS_TABLE')
boardsTable = os.getenv('APPWRITE_BOARDS_TABLE')

# This Appwrite function will be executed every time your function is triggered
def main(context):

    """ context.log("=== INCOMING REQUEST DEBUG ===")
    context.log(f"Request method: {context.req.method}")
    context.log(f"Request headers: {json.dumps(dict(context.req.headers), indent=2)}")
    context.log(f"Request query params: {json.dumps(context.req.query, indent=2)}")
    context.log(f"Request body (raw): {context.req.body}")
    
    # Try to parse body as JSON if it exists
    if context.req.body:
        try:
            parsed_body = json.loads(context.req.body) if isinstance(context.req.body, str) else context.req.body
            context.log(f"Request body (parsed): {json.dumps(parsed_body, indent=2)}")
        except Exception as e:
            context.log(f"Could not parse body as JSON: {str(e)}")
    
    context.log("=== END REQUEST DEBUG ===") """
    #payload = json.loads(context.req.body) if isinstance(context.req.body, str) else context.req.body
    payload = json.loads(context.req.query) if isinstance(context.req.query, str) else context.req.query

    grades = []

    client = (
        Client()
        .set_endpoint(os.environ["APPWRITE_FUNCTION_API_ENDPOINT"])
        .set_project(os.environ["APPWRITE_FUNCTION_PROJECT_ID"])
        .set_key(context.req.headers["x-appwrite-key"])
    )

    tablesDB = TablesDB(client)


    context.log(f"{context.req}")
    climb_data = payload['climbId']
    climbId = climb_data.get('$id')
    context.log(f"Updating grade for {climbId}")

    climb = tablesDB.get_row(
        database_id = databaseId,
        table_id = climbsTable, 
        row_id = climbId 
    )

    boardId = climb['boardId']
    print(boardId)

    board = tablesDB.get_row(
        database_id = databaseId,
        table_id = boardsTable,
        row_id = boardId
    )

    currentGrade = climb['grade']
    communityGrading = board['communityGrading']
    print(currentGrade)
    print(communityGrading)
    
    if communityGrading == False and currentGrade != 0:
        context.log(f"Message: Community grading is off. No updated made")
        return

    queryGrades = tablesDB.list_rows(
        database_id = databaseId,
        table_id = loggedClimbsTable,
        queries = [
            Query.equal('climbId', climbId),
            Query.select(['climbGrade'])
        ]
    )

    #Make a list of all the grade values
    for grade in queryGrades['rows']:
        grades.append(grade['climbGrade'])

    #Round average value to lower number (i.e. 3.9 => 3)
    averageGrade = int(sum(grades)/len(grades))
    update_data = {'grade': averageGrade}

    #Update climb grade according to result
    tablesDB.update_row(
        database_id = databaseId,
        table_id = climbsTable,
        row_id = climbId,
        data = update_data
    ); 

    context.log(f"Message: Climb grade updated to {averageGrade}")

    return
