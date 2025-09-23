class SimpleRequirementsAnalyzer:
  # defining the init of This Agent
  def __init__(self):
    self.name = "Simple Requirements Analyzer"
    self.version = "1.0.0"
    print("Starting Simple Requirements Analyzer Agent...")
  #Practicing with methods with OOP
  def say_hello(self):
    print(f"Hello , I'm {self.name} version {self.version}")
  def analyze_requirements_message(self,message : str):
      """
        Analyze a message in the simplest possible way
        
        Args:
            message: The user's message
            
        Returns:
            A dictionary with basic analysis
        """
      print(f"Analyzing Message :{message}")
      # Retrieving result message

      result = {
         'message' :message,
         'len_message' :len(message),
         'has_question' : '?' in message,
         'seems_urgent' : any(word in message.lower() for word in ['urgent','immediately','asap','important','critical']),
         'seems_polite' :any(word in message.lower() for word in ['please','thank you','appreciate','grateful','excuse me','kindly']),
         'status' :'Analyzed'
      }
      return result



messages = [
  "I need a bus to Tel Aviv ASAP!",
  "Please find me the fastest route to the beach, thank you!",
  "Is there a bus running to Jerusalem on Saturday?",
  "Urgent! I missed my bus, what should I do?",
  "Kindly provide information about bus schedules."
]

# trying the class
analyzer =SimpleRequirementsAnalyzer()
# trying the method
analyzer.say_hello()
# list comphernsive , analyziing the requirments messages
results = [analyzer.analyze_requirements_message(message) for message in messages]

for result in results:
   print(result)
   print()


  
  