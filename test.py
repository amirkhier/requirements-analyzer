"""
Test script to verify all dependencies and API connections
"""
import os
import sys
from pathlib import Path

def test_imports():
    """Test if all required packages are installed"""
    print("🔧 Testing package imports...")
    
    try:
        import django
        print(f"✅ Django {django.get_version()}")
        
        import rest_framework
        print("✅ Django REST Framework")
        
        import psycopg2
        print("✅ PostgreSQL adapter")
        
        import celery
        print(f"✅ Celery {celery.__version__}")
        
        import redis
        print("✅ Redis")
        
        import openai
        print(f"✅ OpenAI {openai.__version__}")
        
        import kafka
        print("✅ Kafka Python")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_environment():
    """Test environment variables"""
    print("\n🔑 Testing environment variables...")
    
    # Load environment from .env file
    env_path = Path(__file__).parent / '.env'
    if env_path.exists():
        print(f"✅ Found .env file at: {env_path}")
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ.setdefault(key.strip(), value.strip())
    else:
        print(f"❌ .env file not found at: {env_path}")
    
    # Check required variables
    required_vars = ['OPENAI_API_KEY', 'SECRET_KEY', 'DATABASE_URL']
    missing_vars = []
    
    for var in required_vars:
        value = os.getenv(var)
        if value:
            # Don't print full API keys for security
            if 'KEY' in var:
                print(f"✅ {var}: {value[:10]}...{value[-4:]}")
            else:
                print(f"✅ {var}: {value}")
        else:
            print(f"❌ {var}: Not found")
            missing_vars.append(var)
    
    return len(missing_vars) == 0

def test_openai_connection():
    """Test OpenAI API connection"""
    print("\n🤖 Testing OpenAI connection...")
    
    try:
        from openai import OpenAI
        
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("❌ OPENAI_API_KEY not found in environment")
            return False
        
        print(f"🔗 Attempting to connect with API key: {api_key[:10]}...{api_key[-4:]}")
        
        # Initialize client without any extra parameters
        client = OpenAI(api_key=api_key)
        
        print("🔄 Making test API call...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say 'Hello FlowBot Requirements Analyzer!' in exactly those words."}
            ],
            max_tokens=50
        )
        
        result = response.choices[0].message.content.strip()
        print(f"✅ OpenAI Response: {result}")
        
        return "Hello FlowBot Requirements Analyzer!" in result
        
    except ImportError as e:
        print(f"❌ Failed to import OpenAI: {e}")
        return False
    except Exception as e:
        print(f"❌ OpenAI connection failed: {e}")
        print(f"   Error type: {type(e).__name__}")
        # Try to provide more helpful error messages
        if "api_key" in str(e).lower():
            print("   💡 This might be an API key issue")
        elif "quota" in str(e).lower():
            print("   💡 This might be a quota/billing issue")
        elif "network" in str(e).lower() or "connection" in str(e).lower():
            print("   💡 This might be a network connectivity issue")
        return False

def main():
    """Run all tests"""
    print("🚀 FlowBot Requirements Analyzer - Setup Test\n")
    
    tests = [
        ("Package Imports", test_imports),
        ("Environment Variables", test_environment),
        ("OpenAI Connection", test_openai_connection)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        print(f"Running: {test_name}")
        print('='*50)
        
        if test_func():
            print(f"🎉 {test_name} PASSED!")
            passed += 1
        else:
            print(f"💥 {test_name} FAILED!")
    
    print(f"\n{'='*50}")
    print(f"FINAL RESULT: {passed}/{total} tests passed")
    print('='*50)
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! Ready to build the Requirements Analyzer!")
        print("\nNext steps:")
        print("1. Create the basic analyzer structure")
        print("2. Implement intent recognition")
        print("3. Add entity extraction")
    else:
        print("🛠️ Some tests failed. Please fix the issues above before continuing.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)