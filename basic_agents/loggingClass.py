"""
Learning about logging - keeping track of what our code does
"""

import logging
from datetime import datetime
from typing import Dict, Any


# Step 1: Set up logging configuration
logging.basicConfig(
    level=logging.DEBUG,  # Show DEBUG level and above
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('requirements_analyzer.log', encoding='utf-8'),  # Save to file
        logging.StreamHandler()  # Also show on screen
    ]
)

#defiing the analyzer class
class LoggingRequirementsAnalyzer:
  """
    An analyzer that keeps detailed logs of everything it does
  """
  def __init__(self):
     # Step 2: Create a logger for this class
    self.logger = logging.getLogger(self.__class__.__name__)
    # defing rest varilbles of class
    self.name = "Logging Requirments Analyzer"
    self.totalMessages_procceed = 0
    self.succesfulAnalysis = 0
    self.failedAnalysis = 0
    #date
    self.startDate = datetime.now()
    # Step 3 - Defining Important Logging
    self.logger.info(f"Starting {self.name} at {self.startDate}")
    self.logger.info("Ready to Analyze Requirements!")
  def analyze_message_with_logging(self,message :str) -> Dict[str,Any]:
     """
        Analyze a message with detailed logging of every step
        
        Args:
            message: The user's message to analyze
            
        Returns:
            Analysis result with logging information
      """
     analysis_id =self.totalMessages_procceed +1
     # Step 4 : Log the start of analysis
     #info of analysis id
     self.logger.info(f"Starting Analysis #{analysis_id}")
     #debuging and checking what value message has
     self.logger.debug(f"Messsage :{message}")
     try:
      # Check if the message is valid:
      if message is None:
        self.logger.warning("Recieved None message.")
        raise ValueError("The message cannot be None.")
      # Check if data type is not string
      if not isinstance(message, str):
        self.logger.warning("Recieved None correct Datatype.")
        raise TypeError("The message must be a string.")
      # Check if there's no characters in messages
      if message.strip() == "":
        self.logger.warning("Recieved Empty Message.")
        raise ValueError("The message cannot be empty or contain only whitespace.")
      # Basic Analysis
      # Basic analysis
      word_count = len(message.split())
      char_count = len(message)
      has_question = '?' in message
      # Advanced analysis with logging
      self.logger.debug(f"Basic Stats : Words counts :{word_count}")
      # defining urgent keywords for classification
      urgent_keywords =['urgent', 'immediately', 'asap', 'important', 'critical']
      seems_urgent = any(word in message for word in urgent_keywords)
      if seems_urgent:
        self.logger.debug("🚨 Detected Urgent message")
      #defiing polite keywords for classification
      polite_keywords = ['please', 'thank you', 'appreciate', 'grateful', 'excuse me', 'kindly']
      seems_polite = any(word in message for word in polite_keywords)
      if seems_polite:
        self.logger.debug("😊 Detected Polite Message")
      #defining greetings keywords for classification
      greeting_keywords = ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening']
      seems_greeting = any(word in message for word in greeting_keywords)
      if seems_greeting:
        self.logger.debug("👋 Detected Greeting Message")
      # Step 7: Create result
      result = {
        'analysis_id' : analysis_id
        ,'message' :message,
        'stats':{
          'word_count' : word_count,
          'char_count' :char_count,
          'has_question' : has_question
        },
        'classification':{
          'seems_urgent' :seems_urgent,
          'seems_polite' :seems_polite,
          'seems_greeting' : seems_greeting
        }
        ,'processed_at' : datetime.now().isoformat()
        ,'status' : 'sucesss'


      }
      # Step 8: Update counters and log success
      self.totalMessages_procceed +=1
      self.succesfulAnalysis +=1
      self.logger.info(f"Message #{analysis_id} has been Analyzed!")
      self.logger.debug(f"Result summary :urgent ={seems_urgent} , poilite ={seems_polite} , greeting={seems_greeting}")

      return result
      
     except ValueError as e:
      # Step 9: Handle and log errors
       self.logger.error(f"Value Error in analysis :#{analysis_id}")
       self.totalMessages_procceed +=1
       self.failedAnalysis +=1
       return {
         'analysis_id' : analysis_id,
         'error' : 'ValueError',
         'error_message' :str(e),
         'processed_at' :datetime.now().isoformat()
         ,'status' :'failed'
       }
     except TypeError as e:
       self.logger.error(f"Type Error in analysis :#{analysis_id}")
       self.totalMessages_procceed +=1
       self.failedAnalysis +=1
       return {
         'analysis_id' : analysis_id,
         'error' : 'TypeError',
         'error_message' :str(e),
         'processed_at' :datetime.now().isoformat()
         ,'status' :'failed'
       }
     except Exception as e:
       self.logger.critical(f"Type Error in analysis :#{analysis_id}")
       self.totalMessages_procceed +=1
       self.failedAnalysis +=1
       return {
         'analysis_id' : analysis_id,
         'error' : 'UnexpectedError',
         'error_message' :str(e),
         'processed_at' :datetime.now().isoformat()
         ,'status' :'failed'
       }
  def get_detailed_stats(self) -> Dict[str, Any]:
    """Get detailed statistics with logging"""
    self.logger.info("Generating detailed stastics :")
    uptime =datetime.now() - self.startDate
    success_rate = (self.succesfulAnalysis / self.totalMessages_procceed if self.totalMessages_procceed > 0 else 0)
    stats = {
       'analyzer_name': self.name,
        'uptime_seconds': uptime.total_seconds(),
        'uptime_formatted': str(uptime),
        'total_processed': self.totalMessages_procceed,
        'successful_analyses': self.succesfulAnalysis,
        'failed_analyses': self.failedAnalysis,
        'success_rate': round(success_rate * 100, 2),
        'start_time': self.startDate.isoformat(),
        'current_time': datetime.now().isoformat()
    }
    self.logger.info(f"📈 Statistics: {self.succesfulAnalysis}/{self.totalMessages_procceed} successful ({stats['success_rate']}%)")
    return stats
  def shutdown(self):
        """Properly shut down the analyzer with final logging"""
        self.logger.info("🔄 Shutting down analyzer...")
        final_stats = self.get_detailed_stats()
        self.logger.info(f"🏁 Final stats: {final_stats}")
        self.logger.info("👋 Analyzer shutdown complete")

if __name__ == "__main__":
    # Step 11: Test our logging analyzer
    # Create analyzer
    analyzer = LoggingRequirementsAnalyzer()

    # Test messages
    test_messages = [
        "Hello! Can you help me find bus schedules please?",
        "I need this information ASAP!",
        "Good morning, what are the routes?",
        "",  # Empty message
        None,  # None value
        "Thank you for your help with the urgent request",
        123,  # Wrong type
    ]

    print(f"\n📝 Testing {len(test_messages)} different messages...")

    for i, message in enumerate(test_messages, 1):
        print(f"\n--- Test {i}: {repr(message)} ---")
        result = analyzer.analyze_message_with_logging(message)

        if result['status'] == 'success':
            print(f"✅ Analysis successful!")
            print(f"   Words: {result['stats']['word_count']}")
            print(f"   Urgent: {result['classification']['seems_urgent']}")
            print(f"   Polite: {result['classification']['seems_polite']}")
        else:
            print(f"❌ Analysis failed")

    # Show final statistics
    print(f"\n📊 Final Statistics:")
    final_stats = analyzer.get_detailed_stats()
    for key, value in final_stats.items():
        print(f"   {key}: {value}")

    # Proper shutdown
    analyzer.shutdown()

    print(f"\n📂 Check 'requirements_analyzer.log' file for detailed logs!")



