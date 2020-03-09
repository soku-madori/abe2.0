from gensim.models import word2vec
import nagisa


def main(word:str):
    try:
        tag = wordClass(word)
        if not tag: return
        selections = wordList(word)
        print(selections)
        flag = '動詞' if tag!='動詞' else '名詞'
        print(flag)
        reword = [i for i in selections if wordclass(i)==flag]
        if reword: return reword[0]
        return 'お前誰た'
    except:
        return 'お前誰だ'


def wordClass(word:str):
    tag = nagisa.tagging(word).postags
    if tag: return tag[0]

def wordList(word:str):
    model = word2vec.Word2Vec.load("word2vec.gensim.model")
    results = model.wv.most_similar(word)
    return [x for y in results for x in y if type(x)==str]



if __name__ == '__main__':
    word = '頑張る'
    print(main(word))
