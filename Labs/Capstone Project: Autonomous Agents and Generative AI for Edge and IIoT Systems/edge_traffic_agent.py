import time
import json
import random
import numpy as np
import paho.mqtt.client as mqtt
import ai_edge_litert.interpreter as tflite # Updated LiteRT import

# Configuration
MQTT_BROKER = "127.0.0.1" 
MQTT_PORT = 1883
MQTT_TOPIC = "smart_city/traffic/intersection_1"
MODEL_PATH = "model.tflite"

# 1. Initialize LiteRT Interpreter
print("Loading AI Model...")
interpreter = tflite.Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def get_sensor_data():
    """Simulate formatting camera data into a NumPy array for the model."""
    # Example: [cars_north_south, cars_east_west]
    return np.array([[random.randint(0, 50), random.randint(0, 50)]], dtype=np.float32)

def autonomous_ai_decision(input_array):
    """Run actual inference using the LiteRT model."""
    # Feed data to the input tensor
    interpreter.set_tensor(input_details[0]['index'], input_array)
    
    # Run the model
    interpreter.invoke()
    
    # Retrieve data from the output tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])[0]
    
    # Map the model's output to an action (Adjust based on how you trained your model)
    actions = ["GREEN_NS", "GREEN_EW", "STANDARD_CYCLE"]
    best_action_index = np.argmax(output_data)
    
    return {
        "action": actions[best_action_index], 
        "duration_seconds": 60 if best_action_index != 2 else 30,
        "confidence": float(output_data[best_action_index])
    }

def main():
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    
    print("Autonomous Edge Agent Active.")
    try:
        while True:
            sensor_array = get_sensor_data()
            ai_output = autonomous_ai_decision(sensor_array)
            
            payload = {
                "timestamp": time.time(),
                "sensors": {"ns_cars": int(sensor_array[0][0]), "ew_cars": int(sensor_array[0][1])},
                "agent_decision": ai_output
            }
            
            client.publish(MQTT_TOPIC, json.dumps(payload))
            print(f"Sensors -> NS: {sensor_array[0][0]}, EW: {sensor_array[0][1]}")
            print(f"Action Executed: {ai_output['action']} (Confidence: {ai_output['confidence']:.2f})")
            
            time.sleep(5) 
            
    except KeyboardInterrupt:
        print("\nAgent offline.")
        client.disconnect()

if __name__ == "__main__":
    main()