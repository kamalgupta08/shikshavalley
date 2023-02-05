from shikshavalley import create_app
import os
import sys
from dotenv import load_dotenv
path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, path)
from shikshavalley.extensions import db
load_dotenv()

app = create_app()
# with app.app_context():
# # # "NURSERY-A","NURSERY-B","LKG-A","LKG-B","UKG-A","UKG-B","1ST-A","1ST-B","2ND-A","2ND-B","3RD","4TH","5TH"
#     from shikshavalley.models import StudentFeesDetails
# #     params={
# #         "class_name":"5TH"
# #     }
# #     result = ClassTypes.new(**params)
# #     db.session.commit()
# #     print (result)
#     db.create_all()

# Starting Flask
if __name__ == '__main__':
    app.run(
        host=os.environ['FLASK_HOST'],
        debug=True if os.environ['FLASK_DEBUG'] == 'True' else False,
        port=os.environ['FLASK_PORT'],
        use_reloader=False
    )