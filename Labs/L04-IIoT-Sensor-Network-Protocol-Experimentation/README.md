## L04: IIoT Sensor Network Design
- What I did: I designed and simulated an Industrial IoT sensor network using Python. I implemented scripts for MQTT, CoAP, and OPC UA protocols to generate and transmit live temperature and humidity data.
- What I learned: I learned the practical trade-offs between protocols: MQTT is efficient for dashboards, CoAP is lightweight for small devices, and OPC UA is the secure "heavyweight" standard for industrial settings.
- Challenges faced: I faced a major issue on my Mac where the GUI real-time graph crashed because I was updating it from the wrong thread; I had to restructure the code to handle data in the background.
