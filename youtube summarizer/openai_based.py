from langchain.document_loaders import youtube
from langchain.text_splitter import RecursiveCharacterTextSplitter
import openai
import streamlit as st


st.set_page_config("YT Summarizer")
st.header = "Your Personal YT summarizer"

url = st.text_input("Enter URL of the youtube video")

if st.button("Submit", type="primary"):
    if url is not None:
        print(url)
        loader =  youtube.YoutubeLoader.from_youtube_url(url)
        docs = loader.load()
        # print(len(docs[0].page_content)) #to know how many characters are there

        ts = RecursiveCharacterTextSplitter(chunk_size = 6000, chunk_overlap = 0)
        final_doc = ts.split_documents(docs)

        # print(len(final_doc))
        temp = []
        for part in final_doc:
            # print(part,end="\n\n")
            openai.api_key = "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"
            response = openai.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = [
                    {"role" :"system","content":"You are an advanced AGI assistant" },
                    {"role" :"user","content":f"summarize the following in to bullet points and make it more simpler{part}" }
                ]
            )
            # print(response)
            msg = response["choices"][0]["messages"]["content"]
            temp.append(msg)
        st.write("".join(temp))