"""
Learning about error handling - making our code safe
"""

class SafeRequirmentsAnalyzer:
    # An analyzer that handles errors gracefully
    def __init__(self):
        self.name = "Safe Requirments Analyzer"
        self.totalMessages_procceed = 0
        self.succesfulAnalysis = 0
        self.failedAnalysis = 0
        print(f"{self.name} initialized!")

    def analyze_message_safely(self, message: str) -> dict:
        """
        Analyze a message with proper error handling

        Args:
            message: The user's message (could be anything!)

        Returns:
            Analysis result or error information
        """
        # Updating every message
        self.totalMessages_procceed += 1

        try:
            # Check if the message is valid:
            if message is None:
                raise ValueError("The message cannot be None.")
            # Check if data type is not string
            if not isinstance(message, str):
                raise ValueError("The message must be a string.")
            # Check if there's no characters in messages
            if message.strip() == "":
                raise ValueError("The message cannot be empty or contain only whitespace.")

            # Retrieving result message
            result = {
                'message': message,
                'len_message': len(message),
                'has_question': '?' in message,
                'seems_urgent': any(word in message.lower() for word in ['urgent', 'immediately', 'asap', 'important', 'critical']),
                'seems_polite': any(word in message.lower() for word in ['please', 'thank you', 'appreciate', 'grateful', 'excuse me', 'kindly']),
                'analysis_number': self.totalMessages_procceed,
                'status': 'success'
            }
            # Adding how many succesfull messages are being added
            self.succesfulAnalysis += 1
            print("Message analyzed successfully!")
            return result

        except ValueError as e:
              # Handle value errors (like empty message)
            self.failedAnalysis += 1
            error_result = {
                'error': 'ValueError',
                'error_message': str(e),
                'analysis_number': self.totalMessages_procceed,
                'status': 'failed'
            }
            print(f"Analysis #{self.totalMessages_procceed}, Error: {e}")
            return error_result

        except TypeError as e:
            # Handle type errors (like wrong data type)
            self.failedAnalysis += 1
            error_result = {
                'error': 'TypeError',
                'error_message': str(e),
                'analysis_number': self.totalMessages_procceed,
                'status': 'failed'
            }
            print(f"Analysis #{self.totalMessages_procceed}, Error: {e}")
            return error_result

        except Exception as e:
            # Handle any other unexpected errors
            self.failedAnalysis += 1
            error_result = {
                'error': 'UnexpectedError',
                'error_message': str(e),
                'analysis_number': self.totalMessages_procceed,
                'status': 'failed'
            }
            print(f"Analysis #{self.totalMessages_procceed}, Error: {e}")
            return error_result
    def get_stats(self) -> dict:
        # getting all statistics of analyzer messages
        stats = {
            'totalMessages_procceed': self.totalMessages_procceed,
            'succesfulAnalysis': self.succesfulAnalysis,
            'failedAnalysis': self.failedAnalysis,
            'success_rate': self.succesfulAnalysis / self.totalMessages_procceed if self.totalMessages_procceed > 0 else 0
        }
        return stats

print("🚀 Testing Safe Requirements Analyzer")
print("=" * 50)
    
    
analyzer = SafeRequirmentsAnalyzer()
    
    # Test with good and bad inputs
test_inputs = [
        "Hello, this is a good message!",      # Good message
        "",                                     # Empty message
        None,                                   # None value
        123,                                    # Wrong type (number)
        "   ",                                  # Just spaces
        "What time is the bus?",                # Good question
        [],                                     # Wrong type (list)
    ]
    
for i, test_input in enumerate(test_inputs):
    print(f"\n--- Test {i+1}: {repr(test_input)} ---")
    result = analyzer.analyze_message_safely(test_input)
    print(f"Result: {result}")
    
# Show final statistics
print(f"\n📊 Final Statistics:")
stats = analyzer.get_stats()
for key, value in stats.items():
    print(f"  {key}: {value}")