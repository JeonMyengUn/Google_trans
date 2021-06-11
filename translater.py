from googletrans import Translator

translator = Translator()

sentence = input("언어를 감지할 문장을 입력해주세요 : ")

result = translator.translate(sentence, 'fr')
detected = translator.detect(sentence)

print(detected.lang,":", sentence)
print(result.dest, ":", result.text)