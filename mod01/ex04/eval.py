class Evaluator:
    def __valid_lists(coefs: list, words: list) -> bool:
        if type(coefs) != list or type(words) != list or len(coefs) != len(words):
            return 0
        if len(list(filter(lambda x: type(x) != float, coefs))) > 0:
            return 0
        if len(list(filter(lambda x: type(x) != str, words))) > 0:
            return 0
        return 1
    @staticmethod
    def zip_evaluate(coefs: list, words: list) -> float:
        if not Evaluator.__valid_lists(coefs, words):
            return -1
        return sum(map(lambda x: len(x[0]) * x[1], zip(words, coefs)))
    @staticmethod
    def enumerate_evaluate(coefs, words) -> float:
        if not Evaluator.__valid_lists(coefs, words):
            return -1
        return sum(map(lambda x: len(x[1]) * coefs[x[0]], enumerate(words)))

if __name__ == '__main__':
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))
    print(Evaluator.enumerate_evaluate(coefs, words))
    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(Evaluator.enumerate_evaluate(coefs, words))
    print(Evaluator.enumerate_evaluate([1.0], ["hello"]))
    print(Evaluator.zip_evaluate([1.0], ["hello"]))
