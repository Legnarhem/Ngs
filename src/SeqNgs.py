__author__ = 'eps'

class SeqNgs:
    """
    Clase que almacena las secuencias cortas de ADN junto a su identificador y su secuencia de calidad asociada
    """
    def __init__(self, id, seq_adn, seq_qual):
        self.id = id
        self.seq_adn = seq_adn
        self.seq_qual = seq_qual

    def seq_len(self):
        """
        Metodo que devuelve la longitud de una secuencia corta de ADN
        :return: entero con la longitud de la secuencia
        """
        return self.seq_adn.length

    def gc_content(self):
        """
        Metodo que devuelve el contenido medio de C y G en una secuencia corta de ADN, en %.
        :return: (float) El % de la media de C y G
        """
        cont_g = 0;
        cont_c = 0;
        for x in (self.seq_adn):
            if x == 'G':
                cont_g += 1
            if x == 'C':
                cont_c += 1
            return ((cont_c + cont_g)/self.seq_adn.length)*100

    def av_qual(self):
        """
        Metodo que devuelve la calidad media de una seguencia corta de ADN
        :return: (float) con la calidad media de la secuencia
        """
        total = 0
        for x in (self.seq_qual):
            total = total + x
        return total/self.seq_len()

    def rev_comp(self):
        """
        Metodo que devuelve la secuencia reversa complementaria de una secuencia de ADN
        :return: secuencia reversa complementaria
        """
        seq_rev = ''
        #Invertimos la cadena y hacemos su complementaria
        for letter in reversed(self.seq_adn):
            if letter == 'A':
                seq_rev += 'T'
            elif letter == 'T':
                seq_rev += 'A'
            elif letter == 'C':
                seq_rev += 'G'
            else:
                seq_rev += 'C'
        return seq_rev

