[
    {
        "id": "9e73241a.7346e8",
        "type": "tab",
        "label": "流程5",
        "disabled": false,
        "info": ""
    },
    {
        "id": "53bdfc4c.e83654",
        "type": "http in",
        "z": "9e73241a.7346e8",
        "name": "",
        "url": "/pin4",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 280,
        "y": 160,
        "wires": [
            [
                "4a51998e.8c62f8"
            ]
        ]
    },
    {
        "id": "8523f023.ab09a",
        "type": "rpi-gpio in",
        "z": "9e73241a.7346e8",
        "name": "GPIO4",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 250,
        "y": 240,
        "wires": [
            [
                "99975bf.048bfa8"
            ]
        ]
    },
    {
        "id": "99975bf.048bfa8",
        "type": "function",
        "z": "9e73241a.7346e8",
        "name": "Set GPIO",
        "func": "global.set(\"GPIO\",msg.payload);\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 450,
        "y": 280,
        "wires": [
            [
                "e48ac74e.9f8a48"
            ]
        ]
    },
    {
        "id": "4a51998e.8c62f8",
        "type": "function",
        "z": "9e73241a.7346e8",
        "name": "Get GPIO",
        "func": "msg.payload=global.get(\"GPIO\");\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 460,
        "y": 200,
        "wires": [
            [
                "8d72e447.c668b8",
                "e48ac74e.9f8a48"
            ]
        ]
    },
    {
        "id": "e48ac74e.9f8a48",
        "type": "debug",
        "z": "9e73241a.7346e8",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 670,
        "y": 300,
        "wires": []
    },
    {
        "id": "8d72e447.c668b8",
        "type": "http response",
        "z": "9e73241a.7346e8",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 670,
        "y": 160,
        "wires": []
    }
]
