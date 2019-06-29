import enum

class Tweet_file_Directory(enum.Enum):
    FA_CUP = 'tweet_parser_result/_FACup'
    SuperTuesday = 'tweet_parser_result/_SuperTuesday'
    USElections = 'tweet_parser_result/_USElections'

class result_Directory(enum.Enum):
    FA_CUP = 'word2vec_result/_FACup'
    SuperTuesday = 'word2vec_result/_SuperTuesday'
    USElections = 'word2vec_result/_USElections'
