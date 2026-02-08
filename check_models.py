import google.generativeai as genai

# Add your Key again here just for the test
genai.configure(api_key="AIzaSyAnYUtuuzWiKeczVndOwVwMwyooWGRkZ80")

print("List of available models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)