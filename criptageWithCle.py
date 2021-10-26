from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
Builder.load_file("criptageWithCle.kv")


class CrypteurWithKeyPage(Widget):
    text_label = StringProperty('Resultat...')

    def crypter(self, cle, text):
        chaine_crypté = ""
        taile_de_cle = len(cle)
        j = 0
        for i in text:
            o = ord(i)
            if j > taile_de_cle-1 or taile_de_cle == 1:
                j = 0
            ok = ord(cle[j])-64
            j += 1
            chaine_crypté += chr(o+ok)
        self.text_label = chaine_crypté

    def decrypter(self, cle, text):
        chaine_decrypte = ""
        taile_de_cle = len(cle)
        taile_de_text = len(text)
        j = 0
        for i in text:
            o = ord(i)
            if j > taile_de_cle-1 or taile_de_cle == 1:
                j = 0
            ok = ord(cle[j])-64
            j += 1
            chaine_decrypte += chr(o-ok)
        self.text_label = chaine_decrypte
