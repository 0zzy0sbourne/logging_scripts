import rospy
from std_msgs.msg import String
import logging 
import os
import time 

def setup_logging(): 
    # Create logs folder if it does not exist 
    if not os.path.exists("logs"): 
        os.makedirs("logs")

    # Remove all contents of the logs folder if it exists and has content
    if os.path.exists("logs"): 
        files = [f for f in os.listdir("logs") if os.path.isfile(os.path.join("logs", f))]
        if len(files) > 0:
            for filename in files:
                file_path = os.path.join("logs", filename)
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Error: {e}")

def write_decision_info_log(decision_info):
    logging.basicConfig(filename="./logs/decision_info.log", level=logging.DEBUG)
    print("DECISION INFO LOGGING STARTED")
    logging.debug(f"{time.asctime(time.localtime(time.time()))}: DECISION INFO: {decision_info}")

def log_callback(data): 
    decision_info = data.data
    write_decision_info_log(decision_info)

def log_subscriber():
    rospy.init_node("decision_logging_node", anonymous=True)
    rospy.Subscriber("/decision_info", String, log_callback)
    rospy.spin()

if __name__ == "__main__":
    setup_logging()
    log_subscriber()
