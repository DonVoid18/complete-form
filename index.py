from selenium import webdriver
import time
import random
driver = webdriver.Chrome()

url = "https://docs.google.com/forms/d/e/1FAIpQLSeBYaLGhOrxemeTrOSYNq1L_BRA-PasQagiUOKXfXowVItexg/viewform"

def select_create_question(question, answer):
        random_question = random.randint(1, answer)

        if question == 8:
            if random_question == 5:
                # escribir en otros las redes sociales (instagrama, ...)
                print("patrick")
        if question == 13:
            if random_question == 4:
                # escribir en otros encentivos que se pueden entregar los voluntarios (dinero, ropa...)
                print("patrick")
        if question == 14:
            if random_question == 1:
                # escribir en otros las redes sociales (instagrama, ...)
                print("patrick")

        template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[{question}]/div/div/div[2]/div/div/span/div/div[{random_question}]/label/div/div[1]/div"
        r = driver.find_element("xpath", template_question)
        r.click()


def quenstion_14_18():
    # Probabilidad de generación
    probabilidad_1 = 0.4  # Probabilidad de generar el número 1
    probabilidad_2 = 0.2  # Probabilidad de generar el número 2
    probabilidad_3 = 0.1  # Probabilidad de generar el número 3
    probabilidad_4 = 0.2  # Probabilidad de generar el número 3
    probabilidad_5 = 0.1  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado = random.choices([1, 2, 3, 4, 5], [probabilidad_1, probabilidad_2, probabilidad_3, probabilidad_4,probabilidad_5], k=1)[0]

    if resultado == 5:
        print("No, no he participado en actividades de voluntariado ambiental en mi comunidad.")
        template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
        r = driver.find_element("xpath", template_question)
        r.click()

        template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div"
        r = driver.find_element("xpath", template_question)
        r.click()

        template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div"
        r = driver.find_element("xpath", template_question)
        r.click()

        template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[1]/div"
        r = driver.find_element("xpath", template_question)
        r.click()

        template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[1]/div"
        r = driver.find_element("xpath", template_question)
        r.click()

        return
    
    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

    # Probabilidad de generación
    probabilidad_2_15 = 0.5  # Probabilidad de generar el número 2
    probabilidad_3_15 = 0.2  # Probabilidad de generar el número 3
    probabilidad_4_15 = 0.2  # Probabilidad de generar el número 3
    probabilidad_5_15 = 0.1  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado_15 = random.choices([2, 3, 4, 5], [probabilidad_2_15, probabilidad_3_15, probabilidad_4_15, probabilidad_5_15], k=1)[0]

    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[{resultado_15}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

    # Probabilidad de generación
    probabilidad_2_16 = 0.4  # Probabilidad de generar el número 2
    probabilidad_3_16 = 0.4  # Probabilidad de generar el número 3
    probabilidad_4_16 = 0.1  # Probabilidad de generar el número 3
    probabilidad_5_16 = 0.1  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado_16 = random.choices([2, 3, 4, 5], [probabilidad_2_16, probabilidad_3_16, probabilidad_4_16, probabilidad_5_16], k=1)[0]

    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/div/span/div/div[{resultado_16}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

    # Probabilidad de generación
    probabilidad_1_17 = 0.4  # Probabilidad de generar el número 1
    probabilidad_2_17 = 0.3  # Probabilidad de generar el número 2
    probabilidad_3_17 = 0.2  # Probabilidad de generar el número 3
    probabilidad_4_17 = 0.1  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado_17 = random.choices([1, 2, 3, 4], [probabilidad_1_17, probabilidad_2_17, probabilidad_3_17, probabilidad_4_17], k=1)[0]

    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[{resultado_17}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

    # Probabilidad de generación
    probabilidad_1_18 = 0.4  # Probabilidad de generar el número 1
    probabilidad_2_18 = 0.2  # Probabilidad de generar el número 2
    probabilidad_3_18 = 0.1  # Probabilidad de generar el número 3
    probabilidad_4_18 = 0.2  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado_18 = random.choices([1, 2, 3, 4], [probabilidad_1_18, probabilidad_2_18, probabilidad_3_18, probabilidad_4_18], k=1)[0]

    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div/span/div/div[{resultado_18}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()
def question_1():
    
   # Probabilidad de generación
    probabilidad_1 = 0.5  # Probabilidad de generar el número 1
    probabilidad_2 = 0.4  # Probabilidad de generar el número 2
    probabilidad_3 = 0.1  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado = random.choices([1, 2, 3], [probabilidad_1, probabilidad_2, probabilidad_3], k=1)[0]

    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

def question_2():
    
    # Probabilidad de generación
    probabilidad_1 = 0.4  # Probabilidad de generar el número 1
    probabilidad_2 = 0.2  # Probabilidad de generar el número 2
    probabilidad_3 = 0.1  # Probabilidad de generar el número 3
    probabilidad_4 = 0.2  # Probabilidad de generar el número 3
    probabilidad_5 = 0.1  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado = random.choices([1, 2, 3,4,5], [probabilidad_1, probabilidad_2, probabilidad_3, probabilidad_4,probabilidad_5], k=1)[0]

    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

def question_3():
    
   # Probabilidad de generación
    probabilidad_1 = 0.3  # Probabilidad de generar el número 1
    probabilidad_2 = 0.3  # Probabilidad de generar el número 2
    probabilidad_3 = 0.2  # Probabilidad de generar el número 3
    probabilidad_4 = 0.2  # Probabilidad de generar el número 3
    probabilidad_5 = 0.1  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado = random.choices([1, 2, 3,4,5], [probabilidad_1, probabilidad_2, probabilidad_3, probabilidad_4,probabilidad_5], k=1)[0]

    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

def question_4():
    
   # Probabilidad de generación
    probabilidad_1 = 0.2  # Probabilidad de generar el número 1
    probabilidad_2 = 0.3  # Probabilidad de generar el número 2
    probabilidad_3 = 0.3  # Probabilidad de generar el número 3
    probabilidad_4 = 0.1  # Probabilidad de generar el número 3
    probabilidad_5 = 0.1  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado = random.choices([1, 2, 3,4,5], [probabilidad_1, probabilidad_2, probabilidad_3, probabilidad_4,probabilidad_5], k=1)[0]

    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

def question_5():
    
  # Probabilidad de generación
    probabilidad_1 = 0.1  # Probabilidad de generar el número 1
    probabilidad_2 = 0.1  # Probabilidad de generar el número 2
    probabilidad_3 = 0.1  # Probabilidad de generar el número 3
    probabilidad_4 = 0.5  # Probabilidad de generar el número 3
    probabilidad_5 = 0.2  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado = random.choices([1, 2, 3,4,5], [probabilidad_1, probabilidad_2, probabilidad_3, probabilidad_4,probabilidad_5], k=1)[0]

    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

def question_6():
    
    # Probabilidad de generación
    probabilidad_1 = 0.5  # Probabilidad de generar el número 1
    probabilidad_2 = 0.2  # Probabilidad de generar el número 2
    probabilidad_3 = 0.1  # Probabilidad de generar el número 3
    probabilidad_4 = 0.1  # Probabilidad de generar el número 3
    probabilidad_5 = 0.1  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado = random.choices([1, 2, 3,4,5], [probabilidad_1, probabilidad_2, probabilidad_3, probabilidad_4,probabilidad_5], k=1)[0]

    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

def question_7():
    
   # Probabilidad de generación
    probabilidad_1 = 0.2  # Probabilidad de generar el número 1
    probabilidad_2 = 0.3  # Probabilidad de generar el número 2
    probabilidad_3 = 0.3  # Probabilidad de generar el número 3
    probabilidad_4 = 0.1  # Probabilidad de generar el número 3
    probabilidad_5 = 0.2  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado = random.choices([1, 2, 3,4,5], [probabilidad_1, probabilidad_2, probabilidad_3, probabilidad_4,probabilidad_5], k=1)[0]

    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

def question_8():
    
   # Probabilidad de generación
    probabilidad_1 = 0.1  # Probabilidad de generar el número 1
    probabilidad_2 = 0.2  # Probabilidad de generar el número 2
    probabilidad_3 = 0.1  # Probabilidad de generar el número 3
    probabilidad_4 = 0.5  # Probabilidad de generar el número 3
    probabilidad_5 = 0.1  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado = random.choices([1, 2, 3, 4, 5], [probabilidad_1, probabilidad_2, probabilidad_3, probabilidad_4, probabilidad_5], k=1)[0]
    # if resultado == 5:
    #     redes_sociales = ["Instagram", "Twitter", "twitter y instragram", "mensaje e de wasap", "Whattsap", "youtube", "videos de youtube" ]
    #     texto = random.choice(redes_sociales)
    #     template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    #     r = driver.find_element("xpath", template_question)
    #     r.send_keys(texto)
    #     print("Otro: ", texto)
    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

def question_9():
    
   # Probabilidad de generación
    probabilidad_1 = 0.2  # Probabilidad de generar el número 1
    probabilidad_2 = 0.4  # Probabilidad de generar el número 2
    probabilidad_3 = 0.1  # Probabilidad de generar el número 3
    probabilidad_4 = 0.1  # Probabilidad de generar el número 3
    probabilidad_5 = 0.1  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado = random.choices([1, 2, 3,4,5], [probabilidad_1, probabilidad_2, probabilidad_3, probabilidad_4,probabilidad_5], k=1)[0]

    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

def question_10():
    
    
    # Probabilidad de generación
    probabilidad_1 = 0.5  # Probabilidad de generar el número 1
    probabilidad_2 = 0.3  # Probabilidad de generar el número 2
    probabilidad_3 = 0.1  # Probabilidad de generar el número 3
    probabilidad_4 = 0.1  # Probabilidad de generar el número 3
    probabilidad_5 = 0.1  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado = random.choices([1, 2, 3, 4, 5], [probabilidad_1, probabilidad_2, probabilidad_3, probabilidad_4, probabilidad_5], k=1)[0]

    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

def question_11():
      
     # Probabilidad de generación
    probabilidad_1 = 0.2  # Probabilidad de generar el número 1
    probabilidad_2 = 0.3  # Probabilidad de generar el número 2
    probabilidad_3 = 0.2  # Probabilidad de generar el número 3
    probabilidad_4 = 0.1  # Probabilidad de generar el número 3
    probabilidad_5 = 0.2  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado = random.choices([1, 2, 3, 4, 5], [probabilidad_1, probabilidad_2, probabilidad_3, probabilidad_4, probabilidad_5], k=1)[0]
  
    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

def question_12():
      
     # Probabilidad de generación
    probabilidad_1 = 0.2  # Probabilidad de generar el número 1
    probabilidad_2 = 0.2  # Probabilidad de generar el número 2
    probabilidad_3 = 0.2  # Probabilidad de generar el número 3
    probabilidad_4 = 0.2  # Probabilidad de generar el número 3
    probabilidad_5 = 0.1  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado = random.choices([1, 2, 3, 4, 5], [probabilidad_1, probabilidad_2, probabilidad_3, probabilidad_4, probabilidad_5], k=1)[0]
  
    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

def question_13():
        
      # Probabilidad de generación
    probabilidad_1 = 0.2  # Probabilidad de generar el número 1
    probabilidad_2 = 0.3  # Probabilidad de generar el número 2
    probabilidad_3 = 0.2  # Probabilidad de generar el número 3
    probabilidad_4 = 0.1  # Probabilidad de generar el número 3
    probabilidad_5 = 0.2  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado = random.choices([1, 2, 3, 4, 5], [probabilidad_1, probabilidad_2, probabilidad_3, probabilidad_4, probabilidad_5], k=1)[0]
    
    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

def question_14():
        
      # Probabilidad de generación
    probabilidad_1 = 0.2  # Probabilidad de generar el número 1
    probabilidad_2 = 0.2  # Probabilidad de generar el número 2
    probabilidad_3 = 0.1  # Probabilidad de generar el número 3
    probabilidad_4 = 0.4  # Probabilidad de generar el número 3
    probabilidad_5 = 0.1  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado = random.choices([1, 2, 3, 4, 5], [probabilidad_1, probabilidad_2, probabilidad_3, probabilidad_4, probabilidad_5], k=1)[0]
    
    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()

def question_14():
        
      # Probabilidad de generación
    probabilidad_1 = 0.2  # Probabilidad de generar el número 1
    probabilidad_2 = 0.2  # Probabilidad de generar el número 2
    probabilidad_3 = 0.1  # Probabilidad de generar el número 3
    probabilidad_4 = 0.4  # Probabilidad de generar el número 3
    probabilidad_5 = 0.1  # Probabilidad de generar el número 3

    # Generar un solo número aleatorio
    resultado = random.choices([1, 2, 3, 4, 5], [probabilidad_1, probabilidad_2, probabilidad_3, probabilidad_4, probabilidad_5], k=1)[0]
    
    template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[{resultado}]/label/div/div[1]/div"
    r = driver.find_element("xpath", template_question)
    r.click()
def complete_form():
  driver.get(url)
  question_1()
  question_2()
  question_3()
  question_4()
  question_5()
  question_6()
  question_7()
  question_8()
  question_9()
  question_10()
  question_11()
  question_12()
  question_13()
  quenstion_14_18()


  # HACER CLICK EN ENVIAR
  time.sleep(1)

  r = driver.find_element("xpath", "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")
  r.click()

  time.sleep(1)

for i in range(20):
  complete_form()
  print(f"completado form {i}")
  time.sleep(1)





  
  