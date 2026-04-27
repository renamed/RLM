import re
import unicodedata

class StringNormalizer:
    """
    Normalizes text strings for NLP preprocessing.

    Applies the following transformations in order:
    1. Lowercase all characters
    2. Remove accents and diacritical marks
    3. Collapse multiple spaces/tabs into single spaces per line
    4. Add space between words and punctuation marks

    Regex patterns are pre-compiled for performance when processing
    large volumes of text.

    Examples
    --------
    >>> normalizer = StringNormalizer()
    >>> normalizer.normalize("Hello   World!")
    'hello world !'
    >>> normalizer.normalize("How are you?")
    'how are you ?'
    >>> normalizer.normalize("Café, por favor!")
    'cafe , por favor !'
    >>> normalizer.normalize("   I hope    you are   well")
    'i hope you are well'
    """

    def __init__(self) -> None:
        """Initialize normalizer with pre-compiled regex patterns."""
        self._multi_space = re.compile(r'[ \t]+')
        self._punct_left = re.compile(r'(\w)([.,!?;:])')
        self._punct_right = re.compile(r'([.,!?;:])(\w)')

    def normalize(self, text: str) -> str:
        """
        Apply full normalization pipeline to input text.

        Parameters
        ----------
        text : str
            Raw input text to normalize.

        Returns
        -------
        str
            Normalized text.
        """
        text = text.lower()
        text = self._remove_accents(text)
        text = self._normalize_whitespace(text)
        text = self._normalize_punctuation_spacing(text)
        return text

    def _remove_accents(self, text: str) -> str:
        """
        Remove accents and diacritical marks from text.

        Uses Unicode NFD normalization to decompose characters
        into base letter + combining diacritical mark,
        then filters out the combining marks.

        Examples
        --------
        >>> self._remove_accents("café")
        'cafe'
        >>> self._remove_accents("ão")
        'ao'

        Parameters
        ----------
        text : str
            Text to remove accents from.

        Returns
        -------
        str
            Text without accents or diacritical marks.
        """
        nfkd = unicodedata.normalize('NFKD', text)
        return ''.join(c for c in nfkd if not unicodedata.combining(c))

    def _normalize_whitespace(self, text: str) -> str:
        """
        Collapse multiple spaces and tabs into one per line.

        Preserves paragraph structure by keeping newline characters.
        Strips leading/trailing whitespace from each line.

        Parameters
        ----------
        text : str
            Text to normalize whitespace in.

        Returns
        -------
        str
            Text with normalized whitespace.
        """
        return '\n'.join(
            self._multi_space.sub(' ', line).strip()
            for line in text.split('\n')
        )

    def _normalize_punctuation_spacing(self, text: str) -> str:
        """
        Insert a single space between words and adjacent punctuation.

        Handles punctuation on both sides:
        - Word followed by punctuation: "hi," becomes "hi ,"
        - Punctuation followed by word: ",there" becomes ", there"

        Punctuation marks handled:  . , ! ? ; :

        Parameters
        ----------
        text : str
            Text to normalize punctuation spacing in.

        Returns
        -------
        str
            Text with spaces around punctuation.
        """
        text = self._punct_left.sub(r'\1 \2', text)
        text = self._punct_right.sub(r'\1 \2', text)
        return text