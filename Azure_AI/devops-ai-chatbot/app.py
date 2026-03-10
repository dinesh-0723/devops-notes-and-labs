# # from fastapi import FastAPI
# # from devops_api import get_pipeline_id, get_pipeline_runs

# # app = FastAPI()

# # @app.get("/pipeline")

# # def pipeline_status(name:str):

# #     pipeline_id = get_pipeline_id(name)

# #     if not pipeline_id:
# #         return {"message":"Pipeline not found"}

# #     runs = get_pipeline_runs(pipeline_id)

# #     result = []

# #     for r in runs:
# #         result.append({
# #             "build_id": r["id"],
# #             "status": r["status"],
# #             "result": r.get("result")
# #         })

# #     return {
# #         "pipeline": name,
# #         "runs": result
# #     }
# from fastapi import FastAPI
# from ai_chat import ask_ai

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message":"DevOps AI Chatbot running"}

# @app.get("/chat")

# def chat(question:str):

#     answer = ask_ai(question)

#     return {"response":answer}
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from devops_api import get_pipeline_id, get_pipeline_runs

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def chatbot_ui():
    with open("templates/chat.html") as f:
        return f.read()


@app.get("/pipeline")

def pipeline_status(name:str):

    pipeline_id = get_pipeline_id(name)

    if not pipeline_id:
        return {"response": "Pipeline not found"}

    runs = get_pipeline_runs(pipeline_id)

    latest = runs[0]

    return {
        "response": f"Latest build status: {latest['result']}"
    }