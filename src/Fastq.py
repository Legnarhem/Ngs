__author__ = 'eps'

class Fastq:
    """
    Clase que almacena las secuencias cortas de ADN junto a su identificador y su secuencia de calidad asociada
    """
    def __init__(self, file):
        self.fastq_file = file
        self.sequences_ngs = None

    def add_sequences(self,sequence):
        """
        Metodo que añade un objeto SeqNgs a la lista de secuencias
        :param sequence: Objeto SeqNgs a añadir
        :return:
        """
        self.sequences_ngs.add(sequence)

    def get_average_qual(self):
        """
        Metodo que devuelve la calidad media de todas las secuencias cortas de ADN guardadas
        :return: (float) con la media de la calidad global
        """
        media = 0
        max = None
        for x in range(0,self.sequences_ngs.length):
            total = 0
            for z in range(0,self.sequences_ngs[x].seq_qual.length):
                total = total + self.sequences_ngs[x].seq_qual[z]
            max[x]=total


        for x in range(0,max.length):
            media = media + max[x]

        return media/max.length
