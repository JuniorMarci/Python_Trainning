def Exportar(TipoDeMeta,Diretoria):

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    from time import sleep
    import os

    # https://www.selenium.dev/selenium/docs/api/py/
    # https://selenium-python.readthedocs.io/locating-elements.html#locating-by-id

    browser = webdriver.Chrome() # Funcionou na Versão 115.0.5790.171 (Versão oficial) 64 bits
    browser.get('https://partage.mereo.com/')
    browser.maximize_window()

    sleep(5)

    usuario = browser.find_element(By.NAME,'txtUser')
    usuario.send_keys('xxx')
    senha = browser.find_element(By.NAME,'txtPsw')
    senha.send_keys('xxx')
    btn = browser.find_element(By.XPATH,'/html/body/form/section[1]/div[3]/input')
    btn.click()
    sleep(10)
    burger = browser.find_element(By.XPATH,'/html/body/div[3]/nav/div/div/ul[1]/li/div/a/img')
    burger.click()
    sleep(3)
    rel_notas = browser.find_element(By.XPATH,'/html/body/sb-root/nav/sb-menu/div/div/perfect-scrollbar/div/div[1]/div/div[5]/a[2]')
    rel_notas.click()
    sleep(5)
    #sel_consolidado = browser.find_element(By.XPATH, "//*[contains(text(), 'Relatório')]")
    #sel_consolidado = browser.find_element(By.XPATH, "//*[contains(@class, 'x-form-cb')]")
    #sel_consolidado.click()
    #browser.find_elements(By.TAG_NAME,'input')
    #browser.quit()

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    from selenium.webdriver.common.action_chains import ActionChains

    def cpt(texto,tag):

        iframe_list = browser.find_elements(By.TAG_NAME, 'iframe')
        for iframe in iframe_list:
            fim = True
            browser.switch_to.frame(iframe)
            lbl = browser.find_elements(By.TAG_NAME, tag)
            for label in lbl:
                if(label.text==texto):
                    location = label.location
                    action = ActionChains(browser)
                    action.move_to_element(label).click().perform()
                    #action.move_by_offset(location['x'], location['y']).click().perform()
                    #print(label,label.location)
                    #action.move_by_offset(label.location).click().perform()
                    print('clicou ',texto)
                    fim = False
                if (fim): cpt(texto,tag)

            browser.switch_to.default_content()



    def npt(campo,insercao):

        iframe_list = browser.find_elements(By.TAG_NAME, 'iframe')
        for iframe in iframe_list:
            fim = True
            browser.switch_to.frame(iframe)
            try:
                campo = browser.find_element(By.NAME,campo)
                campo.send_keys(insercao)
                fim = False

            except: print('Não')

            browser.switch_to.default_content()


    cpt(TipoDeMeta,'label')
    sleep(1)
    cpt('Selecione um registro...','span')
    sleep(2)
    cpt(Diretoria,'span')
    sleep(1)
    cpt('Ok','span')
    sleep(2)

    npt('dfDtCorte','08/2023')

    cpt('Executar','span')
    sleep(2)
    Acompanhamento = browser.find_element(By.ID,'tab-1013-btnInnerEl')
    Acompanhamento.click()
    print('clicou Acompanhamento')
    sleep(5)

    Tab = browser.find_element(By.ID,'gridview-1015')
    Coluna = Tab.find_elements(By.CSS_SELECTOR,"td.x-grid-cell-col2")
    numeros = [int(x.text) for x in Coluna]
    Linha = 'gridview-1015-record-'+str(max(numeros))
    Linha = browser.find_element(By.ID,Linha).click()
    print("Clicou na linha")
    sleep(10)
    Exportar = 'lnk'+str(max(numeros))
    x = False
    while (x==False):
        try:
            Exportar = browser.find_element(By.ID,Exportar).click()
            x = True
        except:
            sleep(0.5)
            print("Não gerado")
    sleep(10)
    Arquivo = 'DataExtract0'+str(max(numeros))+'.xlsx'
    Arquivo = 'C:\\Users\\marcio.souza\\Downloads\\'+Arquivo
    if(Diretoria == '1 - Presidência - Partage ADM'): Nome = 'Consolidada_Presidencia.xlsx'
    if(Diretoria == '2 - Empreendimentos'): Nome = 'Consolidada_Empreendimentos.xlsx'
    sleep(0.5)
    x = False
    while (x==False):
        try:
            os.rename("C:\\Users\\marcio.souza\\Partage\\#Sistemas e Qualidade - Documentos\\Análise de Metas - BI\\Correções (V2)\\Entradas_Mereo\\"+Nome,'C:\\Users\\marcio.souza\\Desktop\\excluir_'+TipoDeMeta+Diretoria)
            x = True
        except:
            sleep(0.5)
            print("Aguardando baixar")
            print(Arquivo)
            print(Nome)
    print('Movido para exclusão')
    sleep(2)
    os.rename(Arquivo, "C:\\Users\\marcio.souza\\Partage\\#Sistemas e Qualidade - Documentos\\Análise de Metas - BI\\Correções (V2)\\Entradas_Mereo\\"+Nome)
    print('Movido para entrada do Mereo')

    browser.quit()

    return False

FinPresidencia = True
while (FinPresidencia):
    print("Iniciado Consolidada Presidência")
    try: FinPresidencia = Exportar ('Relatório de Notas Consolidadas','1 - Presidência - Partage ADM')
    except: 1==1

FinEmpree = True
while (FinEmpree):
    print("Iniciado Consolidada Empreendimentos")
    try: FinEmpree = Exportar ('Relatório de Notas Consolidadas','2 - Empreendimentos')
    except: 1==1





'''

Exportar('Relatório de Notas por Meta','1 - Presidência - Partage ADM')
Exportar('Relatório de Notas por Meta','2 - Empreendimentos')

'''

#cpt('Relatório de Notas Consolidadas','label')


#Exportar('Relatório de Notas Consolidadas','1 - Presidência - Partage ADM')



'''
inputs = browser.find_elements(By.TAG_NAME,'label')
for c in inputs:
    try:
	   #c.execute_script("arguments[0].click();", radio_button)
        print(c.location)
        print(c," foi!")
    except:
        print(c,"falhou")
'''


'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Wait for the page to fully load
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'label')))

# Find the labels
inputs = browser.find_elements(By.TAG_NAME, 'label')
'''


'''
from selenium.webdriver.common.action_chains import ActionChains
action = ActionChains(browser)
action.move_by_offset(x, y).click().perform()
'''