from flask import Flask, request
import os
import upload_video
import save_video
import get_break

app = Flask(__name__)


@app.route('/video', methods=['GET'])
def hello_world():
    print('save video')
    save_video.save_vi()

    print('upload video')
    vid = upload_video.upload_vi()

    return 'hello'


@app.route('/list', methods=['GET'])
def break_list():
    f = open('vids.txt', 'r')

    while True:
        line = f.readline()

        if line == None:
            break

        break_result = get_break.get_break_data(line)
        print(break_result)

    f.close()
    return {'result': break_result}

if __name__ == '__main__':
    app.run(host='0.0.0.0')
