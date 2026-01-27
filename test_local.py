import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Mock Context Class
class MockContext:
    class MockReq:
        def __init__(self, query_params):
            self.query = query_params
            self.headers = {
                "x-appwrite-key": os.getenv("APPWRITE_API_KEY")
            }
            self.method = 'GET'
    
    class MockRes:
        def json(self, data, status=200):
            print(f"\n{'='*60}")
            print(f"✓ Response Status: {status}")
            print(f"✓ Response Data:")
            import json
            print(json.dumps(data, indent=2))
            print(f"{'='*60}\n")
            return data
    
    def __init__(self, query_params=None):
        self.req = self.MockReq(query_params or {})
        self.res = self.MockRes()
    
    def log(self, message):
        print(f"📋 [LOG] {message}")
    
    def error(self, message):
        print(f"❌ [ERROR] {message}")


# Set Appwrite environment variables
os.environ['APPWRITE_FUNCTION_API_ENDPOINT'] = os.getenv('APPWRITE_FUNCTION_API_ENDPOINT')
os.environ['APPWRITE_FUNCTION_PROJECT_ID'] = os.getenv('APPWRITE_FUNCTION_PROJECT_ID')

# Import your main function
from src.main import main

print("\n" + "="*60)
print("🧪 TESTING APPWRITE FUNCTION LOCALLY")
print("="*60 + "\n")

# Test with a valid climb ID
# IMPORTANT: Replace this with an actual climb ID from your database
TEST_CLIMB_ID = "697284d1dcfc18d96aae"

print(f"Testing with Climb ID: {TEST_CLIMB_ID}\n")

context = MockContext({'climbGrade': 13, 'climbedAtAngle': 30, 'comment': '', 'climbRating': None, '$id': '6976f48337bd423ac92a', '$permissions': ['read("user:697009b609618d06d61f")', 'update("user:697009b609618d06d61f")', 'delete("user:697009b609618d06d61f")'], '$createdAt': '2026-01-26T04:58:43.730+00:00', '$updatedAt': '2026-01-26T04:58:43.730+00:00', '$sequence': 16, 'climbId': {'climbName': 'Beyond the Zenith', 'setAtAngle': 30, 'matchAllowed': False, 'setterNotes': 'All zenith holds for hands', 'ascents': 8, 'climbStyle': [], 'climbRating': None, 'grade': 17, '$id': '697284d1dcfc18d96aae', '$sequence': 1, '$createdAt': '2026-01-22T20:13:06.298+00:00', '$updatedAt': '2026-01-26T04:56:32.376+00:00', '$permissions': ['read("user:697009b609618d06d61f")', 'update("user:697009b609618d06d61f")', 'delete("user:697009b609618d06d61f")'], 'setBy': {'username': 'Inversion_Zach', 'igHandle': 'zach_costello_', 'isPrivate': True, 'gradeSystem': 'Hueco', '$id': '697009b609618d06d61f', '$sequence': 1, '$createdAt': '2026-01-20T23:03:19.502+00:00', '$updatedAt': '2026-01-23T21:03:14.603+00:00', '$permissions': ['read("user:697009b609618d06d61f")', 'update("user:697009b609618d06d61f")', 'delete("user:697009b609618d06d61f")'], '$databaseId': '690acc180012566b56c2', '$tableId': 'users'}, 'faBy': {'username': 'Inversion_Zach', 'igHandle': 'zach_costello_', 'isPrivate': True, 'gradeSystem': 'Hueco', '$id': '697009b609618d06d61f', '$sequence': 1, '$createdAt': '2026-01-20T23:03:19.502+00:00', '$updatedAt': '2026-01-23T21:03:14.603+00:00', '$permissions': ['read("user:697009b609618d06d61f")', 'update("user:697009b609618d06d61f")', 'delete("user:697009b609618d06d61f")'], '$databaseId': '690acc180012566b56c2', '$tableId': 'users'}, 'boardId': {'boardName': 'Inversion Tester', 'boardAngle': 30, 'boardType': 'home', 'boardRules': None, 'communityGrading': True, '$id': '697282f0b45cd8950f20', '$sequence': 16, '$createdAt': '2026-01-22T20:06:38.388+00:00', '$updatedAt': '2026-01-23T21:03:38.443+00:00', '$permissions': ['read("user:697009b609618d06d61f")', 'update("user:697009b609618d06d61f")', 'delete("user:697009b609618d06d61f")'], '$databaseId': '690acc180012566b56c2', '$tableId': 'boards'}, '$databaseId': '690acc180012566b56c2', '$tableId': 'climbs'}, 'climbedBy': {'username': 'Inversion_Zach', 'igHandle': 'zach_costello_', 'isPrivate': True, 'gradeSystem': 'Hueco', '$id': '697009b609618d06d61f', '$sequence': 1, '$createdAt': '2026-01-20T23:03:19.502+00:00', '$updatedAt': '2026-01-23T21:03:14.603+00:00', '$permissions': ['read("user:697009b609618d06d61f")', 'update("user:697009b609618d06d61f")', 'delete("user:697009b609618d06d61f")'], 'savedBoards': [], 'savedClimbLists': [], 'homeBoards': [{'isPrivate': False, '$id': '697282f0b45cd8950f20', '$sequence': 10, '$createdAt': '2026-01-22T20:06:38.404+00:00', '$updatedAt': '2026-01-22T20:06:38.404+00:00', '$permissions': ['read("user:697009b609618d06d61f")', 'update("user:697009b609618d06d61f")', 'delete("user:697009b609618d06d61f")'], '$databaseId': '690acc180012566b56c2', '$tableId': 'homeboards'}, {'isPrivate': False, '$id': '69743879980e104f436b', '$sequence': 13, '$createdAt': '2026-01-24T03:12:48.556+00:00', '$updatedAt': '2026-01-24T03:12:48.556+00:00', '$permissions': ['read("user:697009b609618d06d61f")', 'update("user:697009b609618d06d61f")', 'delete("user:697009b609618d06d61f")'], '$databaseId': '690acc180012566b56c2', '$tableId': 'homeboards'}], '$databaseId': '690acc180012566b56c2', '$tableId': 'users'}, '$databaseId': '690acc180012566b56c2', '$tableId': 'logged_climbs'}
)
result = main(context)

print("\n" + "="*60)
print("✅ Test Complete!")
print("="*60 + "\n")