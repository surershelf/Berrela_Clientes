import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from Funcoes import *
import datetime

colorBG = "#f3e9dc"#"#f1e0c5"#"#e6af2e"amarelo#"#2c6e49" verde
colorLabel ="#c08552"#"#c9b79c"#"#e0e2db"#"#4c956c" verde
colorLetter= "#5e3023"#"#71816d"#"#191716"#"#fefee3" verde
fonteMenor = ("Serif", 14)
fonteMaior = ("Serif", 19)
fonteBigger = ("Serif", 25)

janela = tk.Tk()
janela.geometry("1920x1080")
janela.title("Pagamento Clientes")
janela.configure(background= colorBG)

arq = "Clientes.txt"
if not ArquivoExiste:
    CriarArquivo(arq)

data_atual = datetime.date.today()
mes = data_atual.month
ano = data_atual.year


arq_mes = f'Clientes Pagos - Mês {mes} Ano {ano}.txt'
if not ArquivoExiste(arq_mes):
    CriarArquivo(arq_mes)

title = tk.Label(janela, text="Berrela Empreendimentos", font=fonteBigger,background=colorBG,fg=colorLetter)
title.place(x=500, y=50)

def adicionarClientes():
    janela.withdraw()
    segundaTela = tk.Toplevel(janela)
    segundaTela.geometry("1920x1080")
    segundaTela.title("Adicionar Clientes")
    segundaTela.configure(bg=colorBG)

    def voltar_janela_anterior(janela_anterior):
        # Destruir a janela atual
        segundaTela.destroy()

        # Exibir a janela anterior
        janela_anterior.deiconify()

    title = tk.Label(segundaTela, text="Berrela Empreendimentos", font=fonteBigger,background=colorBG,fg=colorLetter)
    title.place(x=500, y=50)

    nome = tk.Label(segundaTela, text="Nome:", font=fonteMaior,background=colorBG,fg=colorLetter)
    nome.place(x=140, y=120)
    inputNome = tk.Entry(segundaTela)
    inputNome.place(x=230, y=129)

    tipoPagamento = tk.Label(segundaTela, text="Qual o tipo (Ap, casa, terreno):", font=fonteMaior,background=colorBG,fg=colorLetter)
    tipoPagamento.place(x=140, y=190)
    inputTipoPagamento = tk.Entry(segundaTela)
    inputTipoPagamento.place(x=500, y=199)

    dataVencim = tk.Label(segundaTela, text="Data de Vencimento da Parcela:", font=fonteMaior,background=colorBG,fg=colorLetter)
    dataVencim.place(x=140, y=260)
    inputDataVencim = tk.Entry(segundaTela)
    inputDataVencim.place(x=514, y=269)

    telefone = tk.Label(segundaTela, text="Telefone:",font=fonteMaior,background=colorBG,fg=colorLetter)
    telefone.place(x=140,y=330)
    inputTelefone = tk.Entry(segundaTela)
    inputTelefone.place(x=255,y=339)

    valorParcela = tk.Label(segundaTela,text="Valor da Parcela: R$",font=fonteMaior,background=colorBG,fg=colorLetter)
    valorParcela.place(x=140,y=400)
    inputValorParcela = tk.Entry(segundaTela)
    inputValorParcela.place(x=385,y=409)


    def salvar():
        try:
            with open(arq, 'a') as a:
                nom = inputNome.get().title()
                tip = inputTipoPagamento.get()
                dat = inputDataVencim.get()
                tel = inputTelefone.get()
                val = inputValorParcela.get()
                if nom and tip and dat and tel and val != " ":
                    a.write(
                        f'{nom.title()}, {tip.title()}, {dat}, {tel}, {val}\n')
                msg = tk.Label(segundaTela,text=f'Novo registro de {nom.title()} adicionado',font=fonteMenor,background=colorLabel,fg=colorLetter)
                msg.place(x=800,y=450)
        except Exception as e:
            msg = tk.Label(segundaTela,text=f'Houve um ERRO na hora de escrever os dados: {e}',font=fonteMenor,background=colorLabel,fg=colorLetter)
            msg.place(x=800,y=450)


    save = tk.Button(segundaTela,text="Salvar",font=fonteMaior,command=salvar,background=colorLabel,fg=colorLetter)
    save.place(x=800,y=500)
    voltar = tk.Button(segundaTela,text="Voltar",font=fonteMaior, command=lambda: voltar_janela_anterior(janela),background=colorLabel,fg=colorLetter)
    voltar.place(x=30,y=30)


def atualizarClientes():
    janela.withdraw()
    terceiraTela = tk.Toplevel(janela)
    terceiraTela.geometry("1920x1080")
    terceiraTela.title("Atualização de Clientes")
    terceiraTela.configure(bg= colorBG)

    def voltar_janela_anterior(janela_anterior):
        # Destruir a janela atual
        terceiraTela.destroy()

        # Exibir a janela anterior
        janela_anterior.deiconify()

    title = tk.Label(terceiraTela, text="Berrela Empreendimentos", font=fonteBigger,background=colorBG,fg=colorLetter)
    title.place(x=500, y=50)

    def att():
        pes = inputPesqCliente.get().title()
        try:
            with open(arq, 'r') as arquivo_orig:
                linhas = arquivo_orig.readlines()

            chave_encontrada = False  # Variável para verificar se a chave de busca foi encontrada
            indice = -1  # Variável para manter o índice da linha que você quer atualizar

            for i, linha in enumerate(linhas.copy(), 1):
                if pes in linha:
                    chave_encontrada = True  # Marca a chave como encontrada
                    indice = i  # Armazena o índice da linha que você quer atualizar

            if chave_encontrada:
                nom, tip, dat, tel, val = linhas[indice - 1].strip().split(',')

                nome = tk.Label(terceiraTela, text="Nome:", font=fonteMaior,background=colorBG,fg=colorLetter)
                nome.place(x=190, y=200)
                inputNome = tk.Entry(terceiraTela)
                inputNome.place(x=280, y=209)
                inputNome.insert(0, nom)

                tipoPagamento = tk.Label(terceiraTela, text="Qual o tipo (Ap, casa, terreno):", font=fonteMaior,background=colorBG,fg=colorLetter)
                tipoPagamento.place(x=190, y=270)
                inputTipoPagamento = tk.Entry(terceiraTela)
                inputTipoPagamento.place(x=550, y=279)
                inputTipoPagamento.insert(0, tip)

                dataVencim = tk.Label(terceiraTela, text="Data de Vencimento da Parcela:", font=fonteMaior,background=colorBG,fg=colorLetter)
                dataVencim.place(x=190, y=340)
                inputDataVencim = tk.Entry(terceiraTela)
                inputDataVencim.place(x=564, y=349)
                inputDataVencim.insert(0, dat)

                telefone = tk.Label(terceiraTela, text="Telefone:", font=fonteMaior,background=colorBG,fg=colorLetter)
                telefone.place(x=190, y=410)
                inputTelefone = tk.Entry(terceiraTela)
                inputTelefone.place(x=305, y=419)
                inputTelefone.insert(0, tel)

                valorParcela = tk.Label(terceiraTela, text="Valor da Parcela: R$", font=fonteMaior,background=colorBG,fg=colorLetter)
                valorParcela.place(x=190, y=480)
                inputValorParcela = tk.Entry(terceiraTela)
                inputValorParcela.place(x=435, y=489)
                inputValorParcela.insert(0, val)

                def attsalva():
                    nonlocal linhas, indice
                    nomatt = inputNome.get()
                    tipatt = inputTipoPagamento.get()
                    datatt = inputDataVencim.get()
                    telatt = inputTelefone.get()
                    valatt = inputValorParcela.get()

                    # Construir a nova linha com as informações atualizadas
                    linhaatt = f"{nomatt},{tipatt},{datatt},{telatt},{valatt}\n"

                    # Substituir a linha antiga com anova linha atualizada
                    linhas[indice - 1] = linhaatt

                    # Escrever todas as linhas de volta no arquivo
                    with open(arq, 'w') as arquivo_atualizado:
                        arquivo_atualizado.writelines(linhas)

                    msg = tk.Label(terceiraTela, text="Cadastro atualizado com sucesso", font=fonteMaior,background=colorLabel,fg=colorLetter)
                    msg.place(x=700, y=400)

                save = tk.Button(terceiraTela, text="Salvar", font=fonteMaior, command=attsalva,background=colorLabel,fg=colorLetter)
                save.place(x=800, y=500)

        except FileNotFoundError:
            msg1 = tk.Label(terceiraTela,text=f"Arquivo '{arq}' não encontrado.",font=fonteMenor,background=colorLabel,fg=colorLetter)
            msg1.place(x=900,y=800)
        except Exception as e:
            msg2 = tk.Label(terceiraTela,text=f"Erro ao atualizar o arquivo: {e}",font=fonteMenor,background=colorLabel,fg=colorLetter)
            msg2.place(x=900, y=800)
        finally:
            arquivo_orig.close()


    voltar = tk.Button(terceiraTela, text="Voltar", font=fonteMaior, command=lambda: voltar_janela_anterior(janela),background=colorLabel,fg=colorLetter)
    voltar.place(x=30, y=30)
    pesqCliente = tk.Label(terceiraTela,text="Pesquise o Cliente:",font=fonteMaior,background=colorBG,fg=colorLetter)
    pesqCliente.place(x=250, y=150)
    inputPesqCliente = tk.Entry(terceiraTela)
    inputPesqCliente.place(x=500,y=159)
    pesqButton = tk.Button(terceiraTela,text="Pesquisar",font=fonteMaior,command=att,background=colorLabel,fg=colorLetter)
    pesqButton.place(x=700, y=140)


def excluirClientes():
    janela.withdraw()
    quartaTela = tk.Toplevel(janela)
    quartaTela.geometry("1920x1080")
    quartaTela.title("Excluir Cliente")
    quartaTela.configure(bg= colorBG)


    def voltar_janela_anterior(janela_anterior):
        # Destruir a janela atual
        quartaTela.destroy()

        # Exibir a janela anterior
        janela_anterior.deiconify()

    title = tk.Label(quartaTela, text="Berrela Empreendimentos", font=fonteBigger,background=colorBG,fg=colorLetter)
    title.place(x=500, y=50)

    nomeExclui = tk.Label(quartaTela,text="Coloque o nome do cliente para excluir:", font=fonteMaior,background=colorBG,fg=colorLetter)
    nomeExclui.place(x=250, y=150)
    inputNomeExclui = tk.Entry(quartaTela)
    inputNomeExclui.place(x=700, y=159)


    def excluir():
        nom = inputNomeExclui.get()
        try:
            with open(arq, 'r') as arquivo_orig:
                linhas = arquivo_orig.readlines()

            chave_encontrada = False  # Variável para verificar se o nome foi encontrado

            with open(arq, 'w') as arquivo_atualizado:
                for linha in linhas:
                    if not chave_encontrada and nom.lower() == linha.split(',')[0].strip().lower():
                        chave_encontrada = True
                    else:
                        arquivo_atualizado.write(linha)

            if chave_encontrada:
                msg = tk.Label(quartaTela,text=f"Registro de '{nom}' excluído com sucesso!",font=fonteMaior,background=colorLabel,fg=colorLetter)
                msg.place(x=500,y=500)
            else:
                msg = tk.Label(quartaTela,text=f"Nome '{nom}' não encontrado no arquivo. Nenhum registro foi excluído.",font=fonteMaior,background=colorLabel,fg=colorLetter)
                msg.place(x=500, y=500)
        except FileNotFoundError:
            msg1 = tk.Label(quartaTela, text=f"Arquivo '{arq}' não encontrado.", font=fonteMaior,background=colorLabel,fg=colorLetter)
            msg1.place(x=400,y=500)
        except Exception as e:
            msg2 = tk.Label(quartaTela,text=f"Erro ao excluir o registro: {e}",font=fonteMaior,background=colorLabel,fg=colorLetter)
            msg2.place(x=400, y=500)

    pesqButton = tk.Button(quartaTela, text="Pesquisar", font=fonteMaior, command=excluir,background=colorLabel,fg=colorLetter)
    pesqButton.place(x=900, y=140)

    voltar = tk.Button(quartaTela, text="Voltar", font=fonteMaior, command=lambda: voltar_janela_anterior(janela),background=colorLabel,fg=colorLetter)
    voltar.place(x=30, y=30)

def adcPagadores():
    janela.withdraw()
    quintaTela = tk.Toplevel(janela)
    quintaTela.geometry("1920x1080")
    quintaTela.title("Excluir Cliente")
    quintaTela.configure(bg= colorBG)

    def voltar_janela_anterior(janela_anterior):
        # Destruir a janela atual
        quintaTela.destroy()

        # Exibir a janela anterior
        janela_anterior.deiconify()

    title = tk.Label(quintaTela, text="Berrela Empreendimentos", font=fonteBigger,background=colorBG,fg=colorLetter)
    title.place(x=500, y=50)

    nomeAdc = tk.Label(quintaTela, text="Coloque o nome para adicionar pagador:", font=fonteMaior,background=colorBG, fg=colorLetter)
    nomeAdc.place(x=250, y=150)
    inputNomeAdc = tk.Entry(quintaTela)
    inputNomeAdc.place(x=750, y=159)

    def adc():
        nom = inputNomeAdc.get().title()
        try:
            with open(arq, 'r') as arquivo_orig:
                linhas = arquivo_orig.readlines()

            chave_encontrada = False  # Variável para verificar se a chave de busca foi encontrada

            with open(arq, 'r'):
                for linha in linhas:
                    if nom in linha:
                        with open(arq_mes, 'a') as pago:
                            pago.write(linha)
                            chave_encontrada = True  # Marca a chave como encontrada
            if chave_encontrada:
                msg = tk.Label(quintaTela,text="Dado atualizado com sucesso!",font=fonteMaior,background=colorLabel,fg=colorLetter)
                msg.place(x=500, y=500)
            else:
                msg = tk.Label(quintaTela,text=f"Chave de busca '{nom}' não encontrada no arquivo. Nenhum registro foi atualizado.",font=fonteMaior,background=colorLabel,fg=colorLetter)
                msg.place(x=500, y=500)

        except FileNotFoundError:
            print(f"Arquivo '{arq}' ou '{arq_mes}' não encontrados.")

        except Exception as e:
            print(f"Erro ao atualizar o arquivo: {e}")

    pesqButton = tk.Button(quintaTela, text="Pesquisar", font=fonteMaior, command=adc,background=colorLabel,fg=colorLetter)
    pesqButton.place(x=900, y=140)

    voltar = tk.Button(quintaTela, text="Voltar", font=fonteMaior, command=lambda: voltar_janela_anterior(janela),background=colorLabel,fg=colorLetter)
    voltar.place(x=30, y=30)


def verCadastros():
    janela.withdraw()
    sextaTela = tk.Toplevel(janela)
    sextaTela.geometry("1920x1080")
    sextaTela.title("Excluir Cliente")
    sextaTela.configure(bg=colorBG)

    sextaTela.grid_columnconfigure(0, weight=1)
    sextaTela.grid_rowconfigure(0, weight=0)
    sextaTela.grid_rowconfigure(1, weight=1)

    msg = tk.Label(sextaTela, text='PESSOAS CADASTRADAS', font=fonteMaior,background=colorBG,fg=colorLetter)
    msg.grid(row=0, column=0, sticky=tk.N)

    text = tk.Text(sextaTela, height=10.0)
    text.grid(row=1, column=0, sticky=tk.NS)

    scrollbar = ttk.Scrollbar(sextaTela, orient="vertical", command=text.yview)
    scrollbar.grid(row=1, column=1, sticky=tk.NS)

    text["yscrollcommand"] = scrollbar.set
    

    def voltar_janela_anterior(janela):
        scrollbar.destroy()
        # Destruir a janela atual
        sextaTela.destroy()

        # Exibir a janela anterior
        janela.deiconify()


    try:
        a = open(arq, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        sextaTela.update()
        linha_count = 50
        total_lines = 0
        for linha in a:
            dado = linha.split(',')
            nome = dado[0].strip()
            tipo_pag = dado[1].strip()
            data = dado[2].strip()
            telefone = dado[3].strip()
            valor_parcela = dado[4].strip()

            # Insert the labels as text into the Text widget
            text.insert(tk.END, f'Nome: {nome}\n')
            text.insert(tk.END, f'Tipo: {tipo_pag}\n')
            text.insert(tk.END, f'Data de Vencimento: {data}\n')
            text.insert(tk.END, f'Telefone: {telefone}\n')
            text.insert(tk.END, f'Valor da Parcela: R${valor_parcela}\n\n')
            text.insert(tk.END, f'------------------------------------------------------------------------------\n\n')

            linha_count += 1
        sextaTela.update_idletasks()


    finally:
        a.close()


        voltar = tk.Button(sextaTela, text="Voltar", font=fonteMaior, command=lambda: voltar_janela_anterior(janela),background=colorLabel,fg=colorLetter)
        voltar.place(x=30, y=30)


def pagamento_Atrasado():
    janela.withdraw()
    setimaTela = tk.Toplevel(janela)
    setimaTela.geometry("1920x1080")
    setimaTela.title("Excluir Cliente")
    setimaTela.configure(bg=colorBG)

    setimaTela.grid_columnconfigure(0, weight=1)
    setimaTela.grid_rowconfigure(0, weight=0)
    setimaTela.grid_rowconfigure(1, weight=1)

    msg = tk.Label(setimaTela, text='PESSOAS QUE NÃO PAGARAM ESTE MÊS', font=fonteMaior,background=colorBG,fg=colorLetter)
    msg.grid(row=0, column=0, sticky=tk.N)

    text = tk.Text(setimaTela, height=10.0)
    text.grid(row=1, column=0, sticky=tk.NS)

    scrollbar = ttk.Scrollbar(setimaTela, orient="vertical", command=text.yview)
    scrollbar.grid(row=1, column=1, sticky=tk.NS)

    text["yscrollcommand"] = scrollbar.set

    def voltar_janela_anterior(janela):
        scrollbar.destroy()
        # Destruir a janela atual
        setimaTela.destroy()

        # Exibir a janela anterior
        janela.deiconify()

    try:
        with open(arq, 'r') as arquivo_orig:
            linhas = arquivo_orig.readlines()
        with open(arq_mes, 'r') as arquivo_orig1:
            linhas1 = arquivo_orig1.readlines()

        pessoas_em_arq1 = set()
        data_atual = datetime.date.today()
        dia_atual = data_atual.day

        for linha1 in linhas1:
            dado1 = linha1.split(',')
            if len(dado1) >= 5:
                nome1 = dado1[0].strip()
                pessoas_em_arq1.add(nome1)

        for linha in linhas:
            dado = linha.split(',')
            if len(dado) >= 5:
                nome = dado[0].strip()
                data = int(dado[2])
                if dia_atual > data:
                    if nome not in pessoas_em_arq1:  # Verifica se o nome não está em arq1
                        tipo_pag = dado[1].strip()
                        telefone = dado[3].strip()
                        valor_parcela = dado[4].strip()

                        text.insert(tk.END, f'Nome: {nome}\n')
                        text.insert(tk.END, f'Tipo: {tipo_pag}\n')
                        text.insert(tk.END, f'Data de Vencimento: {data}\n')
                        text.insert(tk.END, f'Telefone: {telefone}\n')
                        text.insert(tk.END, f'Valor da Parcela: R${valor_parcela}\n\n')
                        text.insert(tk.END,
                                    f'------------------------------------------------------------------------------\n\n')


    except FileNotFoundError:
        print(f"Arquivo '{arq}' ou '{arq_mes}' não encontrado.")
    except Exception as e:
        print(f"Erro!!! {e}")
    finally:
        arquivo_orig.close()
        arquivo_orig1.close()
    voltar = tk.Button(setimaTela, text="Voltar", font=fonteMaior, command=lambda: voltar_janela_anterior(janela),background=colorLabel,fg=colorLetter)
    voltar.place(x=30, y=30)


adicionarClientes = tk.Button(janela, text="Adicionar Clientes", font=fonteMaior, width=17, height=1,
                              command=adicionarClientes,background=colorLabel,fg=colorLetter)
adicionarClientes.place(x=280, y=200)

atualizarClientes = tk.Button(janela, text="Atualizar Clientes", font=fonteMaior, width=17, height=1,
                              command=atualizarClientes,background=colorLabel,fg=colorLetter)
atualizarClientes.place(x=280, y=350)

excluirClientes = tk.Button(janela, text="Excluir Clientes", font=fonteMaior, width=17, height=1,
                            command=excluirClientes,background=colorLabel,fg=colorLetter)
excluirClientes.place(x=280, y=500)

adicionarPagadores = tk.Button(janela, text="Adicionar Pagadores", font=fonteMaior, width=17, height=1,
                               command=adcPagadores,background=colorLabel,fg=colorLetter)
adicionarPagadores.place(x=850, y=200)

verCadastros = tk.Button(janela, text="Ver Cadastros", font=fonteMaior, width=17, height=1,
                         command=verCadastros,background=colorLabel,fg=colorLetter)
verCadastros.place(x=850, y=350)

verAtrasados = tk.Button(janela, text="Ver Atrasados", font=fonteMaior, width=17, height=1,
                         command=pagamento_Atrasado,background=colorLabel,fg=colorLetter)
verAtrasados.place(x=850, y=500)

janela.mainloop()


