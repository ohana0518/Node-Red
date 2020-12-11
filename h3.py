[
    {
        "id": "afb870b3.53aa2",
        "type": "tab",
        "label": "流程3",
        "disabled": false,
        "info": ""
    },
    {
        "id": "1a8d5694.d80f49",
        "type": "inject",
        "z": "afb870b3.53aa2",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "",
        "crontab": "",
        "once": true,
        "onceDelay": "0",
        "x": 160,
        "y": 180,
        "wires": [
            [
                "971abfa0.f692b"
            ]
        ]
    },
    {
        "id": "971abfa0.f692b",
        "type": "function",
        "z": "afb870b3.53aa2",
        "name": "Payload",
        "func": "msg.headers={\n    \n    \n    deviceKey:\"tRVKz5CU7qm0e3bg\"\n};\nmsg.payload=\"ohana,,24.5\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 350,
        "y": 220,
        "wires": [
            [
                "d35a5b91.81b798"
            ]
        ]
    },
    {
        "id": "43b9d79d.1936a8",
        "type": "http response",
        "z": "afb870b3.53aa2",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 560,
        "y": 360,
        "wires": []
    },
    {
        "id": "5849091a.7bcdb8",
        "type": "debug",
        "z": "afb870b3.53aa2",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "x": 500,
        "y": 540,
        "wires": []
    },
    {
        "id": "d35a5b91.81b798",
        "type": "http request",
        "z": "afb870b3.53aa2",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "paytoqs": false,
        "url": "https://api.mediatek.com/mcs/v2/devices/DBr1jJuH/datapoints.csv",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "x": 280,
        "y": 400,
        "wires": [
            [
                "43b9d79d.1936a8",
                "5849091a.7bcdb8"
            ]
        ]
    }
]
