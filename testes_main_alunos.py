import unittest
from datetime import datetime
from app import obter_resposta


class TestObterResposta(unittest.TestCase):
    def teste_saudacoes(self):
        """Teste de respostas a saudações - 3 testes"""
        self.assertEqual(obter_resposta("olá"), "Olá tudo bem!")
        self.assertEqual(obter_resposta("bom dia"), "Olá tudo bem!")
        self.assertEqual(obter_resposta("boa tarde"), "Olá tudo bem!")

    def teste_perguntas_simples(self):
        """Teste de respostas a perguntas simples - 4 testes"""
        self.assertEqual(obter_resposta("como estás"), "Estou bem, obrigado!")
        self.assertEqual(obter_resposta("estás bem?"), "Estou bem, obrigado!")
        self.assertEqual(obter_resposta("tudo bem?"), "Estou bem, obrigado!")
        self.assertEqual(obter_resposta("como vais?"), "Estou bem, obrigado!")

    def teste_despedidas(self):
        """Teste de respostas a despedidas - 3 testes"""
        self.assertEqual(obter_resposta("bye"), "Gostei de falar contigo! Até breve...")
        self.assertEqual(obter_resposta("adeus"), "Gostei de falar contigo! Até breve...")
        self.assertEqual(obter_resposta("até logo"), "Gostei de falar contigo! Até breve...")

    def teste_historia_portugal(self):
        """Teste de respostas sobre história de Portugal - 1 teste"""
        self.assertEqual(obter_resposta("história de Portugal"), "Portugal tem uma rica história que inclui a Era dos Descobrimentos...")

    def teste_cozinhar(self):
        """Teste de respostas sobre cozinhar - 1 teste"""
        self.assertEqual(obter_resposta("gostas de cozinhar?"), "Sim, cozinhar pode ser uma atividade muito relaxante e criativa.")

    def teste_programar(self):
        """Teste de respostas sobre programar - 2 testes"""
        self.assertEqual(obter_resposta("sabes programar?"), "Sim, sei programar em várias linguagens como Python, JavaScript e outras.")
        self.assertEqual(obter_resposta("o que é programar?"), "Programar é escrever instruções para que um computador execute tarefas específicas.")

    def teste_desenvolvimento(self):
        """Teste de respostas sobre desenvolvimento - 4 testes"""
        self.assertEqual(obter_resposta("desenvolvimento web"), "O desenvolvimento web envolve a criação de sites e aplicações web...")
        self.assertEqual(obter_resposta("desenvolvimento de software"), "O desenvolvimento de software inclui análise, design, codificação e testes.")
        self.assertEqual(obter_resposta("desenvolvimento front-end"), "Front-end refere-se à parte visual de um site com a qual os utilizadores interagem.")
        self.assertEqual(obter_resposta("desenvolvimento back-end"), "Back-end refere-se ao servidor, base de dados e lógica de aplicação.")

    def teste_ia(self):
        """Teste de respostas sobre inteligência artificial - 3 testes"""
        resposta_esperada = "A inteligência artificial é um campo da ciência da computação que se concentra na criação de sistemas que podem realizar tarefas que normalmente requerem inteligência humana."
        self.assertEqual(obter_resposta("ia"), resposta_esperada)
        self.assertEqual(obter_resposta("inteligência artificial"), resposta_esperada)
        self.assertEqual(obter_resposta("o que é IA?"), resposta_esperada)

    def teste_saude(self):
        """Teste de respostas sobre saúde - 3 testes"""
        resposta = "A saúde é um estado de completo bem-estar físico, mental e social, e não apenas a ausência de doenças ou enfermidades."
        self.assertEqual(obter_resposta("saúde"), resposta)
        self.assertEqual(obter_resposta("importância da saúde"), resposta)
        self.assertEqual(obter_resposta("o que é saúde?"), resposta)

    def teste_indisposicao(self):
        """Teste de respostas sobre indisposição - 3 testes"""
        resposta = "Sintomas de indisposição podem incluir fadiga, dor de cabeça, náusea e outros sinais de que algo não está bem."
        self.assertEqual(obter_resposta("indisposição"), resposta)
        self.assertEqual(obter_resposta("estou com indisposição"), resposta)
        self.assertEqual(obter_resposta("sinto indisposição"), resposta)

    def teste_horas_e_data(self):
        """Teste de respostas a perguntas sobre horas e data"""
        hora_atual = datetime.now().strftime("%H:%M")
        data_atual = datetime.now().strftime("%d-%m-%Y")

        self.assertEqual(obter_resposta("que horas são"), f"São: {hora_atual} horas")
        self.assertEqual(obter_resposta("qual é a data"), f"Hoje é dia: {data_atual}")

    def teste_resposta_padrao(self):
        """Teste de resposta padrão para entradas não reconhecidas"""
        self.assertEqual(obter_resposta("xyz123"), "Desculpa, não entendi a questão! xyz123")
        self.assertEqual(obter_resposta("teste123"), "Desculpa, não entendi a questão! teste123")
        self.assertEqual(obter_resposta("coisa aleatória"), "Desculpa, não entendi a questão! coisa aleatória")
        self.assertEqual(obter_resposta("fala comigo"), "Desculpa, não entendi a questão! fala comigo")


if __name__ == '__main__':
    unittest.main()