from flask import Flask, render_template, request, Markup,jsonify
from model import predict_image
import utils
import api_res
import base64 as b4
import cv2
cam=cv2.VideoCapture(1)
result,image=cam.read()
if result:
      img=image

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/api',methods = ['GET','POST'])
def api():
    try:
            file = request.files['image']
            # Read the image via file.stream
            # img = file.read()

            prediction = predict_image(img)
            print(prediction)
            res = Markup(api_res.disease_dic[prediction])
            print(res)
            return jsonify(str(res))
    except Exception as e:
                print(e)
                return jsonify(str(e))
    return jsonify('server is busy')







@app.route('/esp',methods = ['GET','POST'])
def esp():
    try:

            print(f'request ===> {request}')
            file = request.data
            #file=json.loads(request.data)
            print(f'file===> {file}')
            # Read the image via file.stream
            #img = file['image']
            #print(f'image ==> {img}')
            decoded = b4.b64decode(file)
            prediction = predict_image(decoded)
            print(prediction)
            res = Markup(api_res.disease_dic[prediction])
            print(res)
            return jsonify(str(prediction))
    except Exception as e:
                print(e)
                return jsonify(str(e))
    #return jsonify('server is busy')  







'''
@app.route('/esp',methods = ['POST'])
def esp():
    try:

            print(f'request ===> {request}')
            j = json.loads(request)
            print(j)
            d = request.data()
            print(d)
            file = request.get_data(True,True)
            print(f'data===> {file}')
            # Read the image via file.stream
            #img = file["image"]
            #print(f'image ==> {img}')
            decoded = b4.b64decode(file)
            prediction = predict_image(decoded)
            print(prediction)
            res = Markup(api_res.disease_dic[prediction])
            print(res)
            return jsonify(str(res))
    except Exception as e:
                print(e)
                return jsonify(str(e))
    #return jsonify('server is busy')  




@app.route('/esp',methods = ['GET','POST'])
def esp():
    try:
            file = request.files['image']
            # Read the image via file.stream
            img = file.read()
            decoded = b4.b64decode(img)
            prediction = predict_image(decoded)
            print(prediction)
            res = Markup(api_res.disease_dic[prediction])
            print(res)
            return jsonify(str(prediction))
    except Exception as e:
                print(e)
                return jsonify(str(e))
    #return jsonify('server is busy') 
'''


'''
@app.route('/esp',methods = ['GET','POST'])
def esp():
    dones = []
    try:
          
            file = request.files['image']
            dones.append('got the image')
            # Read the image via file.stream
            img = file.read()
            dones.append('read the image')
            decoded = b4.b64decode(img)
            dones.append('docoded')
            prediction = predict_image(decoded)
            dones.append('predicted')
            print(prediction)
            res = Markup(api_res.disease_dic[prediction])
            print(res)
           
    except Exception as e:
                print(e)
                return jsonify(str(dones)+str(e))
                #return jsonify(str(e))
    #return jsonify('server is busy')  
'''

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            file = request.files['file']
            img = file.read()
            prediction = predict_image(img)
            print(prediction)
            res = Markup(utils.disease_dic[prediction])
            return render_template('results.html', status=200, result=res)
        except:
            pass
    return render_template('index.html', status=500, res="Internal Server Error")


@app.route('/weather', methods = ['GET'])
def weather():
    return render_template('weather.html')

@app.route('/pre',methods = ['GET'])
def pre():
    return render_template('server.html')

@app.route('/about',methods = ['GET',])
def about():
    return render_template('about.html')

@app.route('/api/test',methods = ['GET','POST'])
def test():
    return jsonify('test successfull')


if __name__ == "__main__":
    app.run(debug=False)
