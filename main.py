from dotenv import load_dotenv



def main():
    load_dotenv()
    openai_api_key = os.getenv("OPEN_API_KEY")
    #print(f"API Key: '{openai_api_key}'")  # Check if it's loading correctly

    
        
        
if __name__ == '__main__':
    main()