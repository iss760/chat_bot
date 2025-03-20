from openai import OpenAI
from openai import AuthenticationError
from dotenv import load_dotenv
import os

load_dotenv()

# OpenAI API 키 설정
api_key = os.getenv('API_KEY')
if not api_key:
    raise ValueError("API_KEY가 설정되지 않았습니다. .env 파일을 확인하세요.")
client = OpenAI(api_key=api_key)

def chat_with_gpt(prompt):
    try:
        # ChatGPT API 호출
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # 또는 "gpt-4" 사용 가능
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        # 응답 추출
        return response.choices[0].message.content
    
    except AuthenticationError:
        return "API 키가 올바르지 않습니다. API 키를 확인해주세요."
    except Exception as e:
        return f"에러가 발생했습니다: {str(e)}"

def main():
    while True:
        # 사용자 입력 받기
        user_input = input("질문을 입력하세요 (종료하려면 'quit' 입력): ")
        
        if user_input.lower() == 'quit':
            break
        
        # ChatGPT API 호출 및 응답 출력
        response = chat_with_gpt(user_input)
        print("\nChatGPT 응답:")
        print(response)
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
