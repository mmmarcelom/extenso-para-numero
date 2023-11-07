import re

def limpar(texto):

  palavra = texto.lower()

  regex_acentos = '[áàâãéèêíïóôõöúüçñ]'

  if not re.search(regex_acentos, palavra) == None:
    
    regex_limpeza = {
        'a':'[áàâã]',
        'e':'[éèê]',
        'i':'[íï]',
        'o':'[óôõö]',
        'u':'[úü]',
        'c':'[ç]',
        'n':'[ñ]'
    }
    
    for vogal in regex_limpeza.keys():
      palavra = re.sub(regex_limpeza[vogal], vogal, palavra)

  palavra = palavra.replace(' e ', ' ')
  return palavra

def converter(numero_extenso):

  algarismos = { 'um': 1, 'dois': 2, 'tres': 3, 'quatro': 4, 'cinco': 5,
      'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10, 'onze': 11,
      'doze': 12, 'treze': 13, 'quatorze': 14, 'catorze':14, 'quinze': 15, 'dezesseis': 16,
      'dezessete': 17, 'dezoito': 18, 'dezenove': 19,'vinte': 20,'trinta': 30,
      'quarenta': 40,'cinquenta': 50,'sessenta': 60,'setenta': 70,'oitenta': 80,
      'noventa': 90,'cem': 100,'cento': 100,'duzentos': 200,'trezentos': 300,
      'quatrocentos': 400,'quinhentos': 500,'seiscentos': 600,'setecentos': 700,
      'oitocentos': 800,'novecentos': 900 }
  
  multiplicadores = {
      'mil': 1000,
      'milhao': 1000000,
      'milhoes': 1000000,
      'bilhao': 1000000000,
      'bilhoes': 1000000000,
      'k': 1000,
      'm': 1000000,
      'g': 1000000000
  }
  
  palavras = limpar(numero_extenso)
  numero = 0
  valor = 0

  if re.search('\d', palavras):

    valor = re.search('[\d,\.]+', palavras).group(0).replace(',','.')
    notacao_cientifica = re.search('[a-z]', palavras).group(0)
    
    numero = float(valor) * multiplicadores[notacao_cientifica]
  else:
    for palavra in palavras.split():

        if palavra in algarismos: 
          valor += algarismos[palavra]
          continue
        
        if palavra in multiplicadores:
          if valor == 0: valor = 1
          valor *= multiplicadores[palavra]
          
          numero += valor
          valor = 0
    
    numero += valor
  return int(numero)