# Dynamic Cards
Rough prototype of digital cards by abstracting key concepts and explanations from a YouTube video. 

Flash cards are effective. Current research shows that digital flash cards are effective study tools with the promotion of active recall or the active engagement in retrieval of data from memory, but Sage et al. (2017) investigated the differences in the range of effectiveness with mode (paper, tablet or labtop). They found that students did not learn as well when viewing flash cards on a computer. However, making your own flashcards is an investment in time and if you are reviewing for board exams the financial cost of purchasing program related materials is burdensome.  In this prototype, I have created digital cards by abstracting key concepts and explanations from a YouTube video.

## Set-Up
### Google Cloud
1) Create a Google Cloud Platform account.
2) Create new project. The associated project ID number will be used to build the application.
3) Enable Vertex AI API.
4) Create service account and download corresponding service account key to be saved with directory which can be add to .gitignore file.

### Running in VS Code terminal
1) Clone GitHub Repository
   ```python 
   git clone https://github.com/remomcc/Quiz-Generator.git
   ```
2) Create virtual environment
   ```python
   python -m venv env
   ```
3) Activate virtual environment
   ```python
   source env/bin/activate
   ```
4) Install requirements for backend
   ```python
   pip install -r requirements.txt
   ```
5) Make sure service account key (named as 'authentication.json' in this case) is in the same directory as the cloned respository.
   ```python
   export GOOGLE_APPLICATION_CREDENTIALS='authentication.json'
   ```   
6) Run application

   Front end:
   ```python
   npm run dev
   ```

   Back end:
   ```python
   uvicorn main:app
   ```
   
## Dynamic cards overview
FastAPI -> YouTube Video Link -> Split the video transcript into documents (chunks of 1000 characters) -> Divide into a sample size of 5 documents per group —> Find the key concepts by feeding into the Gemini Pro large language model via Vertex AI -> Convert output into a Python dictionary —> Display cards

## Loom presentation
#https://www.loom.com/share/632e758ea49e42d19bf3f3b02d62425a

#https://pitch.com/v/ai-dynamocards-making-motivation-utility-8jd597

## Time allocated for this project
30-40 hours. The most difficult aspect of this project was cleaning the json string. Regex needed to be used; assistance provided by ChatGPT.

## Special thanks 
Thank you to Radical AI's Mikhail, Saqib and ReX as well as ChatGPT.

## References
CS50. (2024, January 1). CS50x 2024 - Lecture 5 - Data Structures. Www.youtube.com. https://www.youtube.com/watch?v=0euvEdPwQnQ

Documentation. (n.d.). Google Cloud. https://cloud.google.com/docs

FastAPI. (n.d.). FastAPI. Fastapi.tiangolo.com. https://fastapi.tiangolo.com/

langchain 0.1.12 — 🦜🔗 LangChain 0.1.12. (n.d.). Api.python.langchain.com. https://api.python.langchain.com/en/latest/langchain_api_reference.html

OpenAI. (2024). ChatGPT. Retrieved May 6, 2024, from https://www.openai.com/chatgpt

Sage, K., Krebs, B., & Grove, R. (2017). Flip, Slide, or Swipe? Learning Outcomes from Paper, Computer, and Tablet Flashcards. Technology, Knowledge and Learning, 24(3), 461–482. https://doi.org/10.1007/s10758-017-9345-9
