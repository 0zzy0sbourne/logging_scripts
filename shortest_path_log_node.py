import rospy
from std_msgs.msg import String
import logging
import os
import time 

def setup_logging():
    # Create the logs folder if it does not exist
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

def write_shortest_path_log(shortest_path):
    logging.basicConfig(filename="./logs/shortest_path.log", level=logging.DEBUG)
    print("SHORTEST PATH LOGGING STARTED")
    logging.debug(f"{time.asctime(time.localtime(time.time()))}: SHORTEST PATH: {shortest_path}")

def log_callback(data): 
    shortest_path = data.data
    write_shortest_path_log(shortest_path)

def log_subscriber(): 
    rospy.init_node('log_subscriber', anonymous=True)
    rospy.Subscriber('shortest_path_topic', String, log_callback)
    rospy.spin()

if __name__ == '__main__': 
    setup_logging()
    log_subscriber()


