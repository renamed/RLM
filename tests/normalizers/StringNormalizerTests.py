import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from normalizers.StringNormalizer import StringNormalizer


class StringNormalizerTests(unittest.TestCase):
    def setUp(self):
        self.normalizer = StringNormalizer()

    # ============================================================
    # _lowercase
    # ============================================================
    def test_lowercase_all_uppercase(self):
        self.assertEqual(
            self.normalizer._lowercase("HELLO WORLD"),
            "hello world"
        )

    def test_lowercase_mixed_case(self):
        self.assertEqual(
            self.normalizer._lowercase("Hello World"),
            "hello world"
        )

    def test_lowercase_with_accents(self):
        self.assertEqual(
            self.normalizer._lowercase("CAFÉ"),
            "café"
        )

    def test_lowercase_cyrillic(self):
        self.assertEqual(
            self.normalizer._lowercase("ПРИВЕТ"),
            "привет"
        )

    def test_lowercase_empty_string(self):
        self.assertEqual(self.normalizer._lowercase(""), "")

    def test_lowercase_numbers_unchanged(self):
        self.assertEqual(
            self.normalizer._lowercase("ABC 123 XYZ"),
            "abc 123 xyz"
        )

    def test_lowercase_punctuation_unchanged(self):
        self.assertEqual(
            self.normalizer._lowercase("HELLO! WORLD?"),
            "hello! world?"
        )

    # ============================================================
    # _remove_accents
    # ============================================================
    # Acute accent
    def test_accents_acute_a(self):
        self.assertEqual(self.normalizer._remove_accents("á"), "a")

    def test_accents_acute_e(self):
        self.assertEqual(self.normalizer._remove_accents("é"), "e")

    def test_accents_acute_i(self):
        self.assertEqual(self.normalizer._remove_accents("í"), "i")

    def test_accents_acute_o(self):
        self.assertEqual(self.normalizer._remove_accents("ó"), "o")

    def test_accents_acute_u(self):
        self.assertEqual(self.normalizer._remove_accents("ú"), "u")

    def test_accents_acute_all_vowels(self):
        self.assertEqual(self.normalizer._remove_accents("áéíóú"), "aeiou")

    # Grave accent
    def test_accents_grave_a(self):
        self.assertEqual(self.normalizer._remove_accents("à"), "a")

    def test_accents_grave_e(self):
        self.assertEqual(self.normalizer._remove_accents("è"), "e")

    def test_accents_grave_i(self):
        self.assertEqual(self.normalizer._remove_accents("ì"), "i")

    def test_accents_grave_o(self):
        self.assertEqual(self.normalizer._remove_accents("ò"), "o")

    def test_accents_grave_u(self):
        self.assertEqual(self.normalizer._remove_accents("ù"), "u")

    def test_accents_grave_all_vowels(self):
        self.assertEqual(self.normalizer._remove_accents("àèìòù"), "aeiou")

    # Circumflex
    def test_accents_circumflex_a(self):
        self.assertEqual(self.normalizer._remove_accents("â"), "a")

    def test_accents_circumflex_e(self):
        self.assertEqual(self.normalizer._remove_accents("ê"), "e")

    def test_accents_circumflex_i(self):
        self.assertEqual(self.normalizer._remove_accents("î"), "i")

    def test_accents_circumflex_o(self):
        self.assertEqual(self.normalizer._remove_accents("ô"), "o")

    def test_accents_circumflex_u(self):
        self.assertEqual(self.normalizer._remove_accents("û"), "u")

    def test_accents_circumflex_all_vowels(self):
        self.assertEqual(self.normalizer._remove_accents("âêîôû"), "aeiou")

    # Tilde
    def test_accents_tilde_a(self):
        self.assertEqual(self.normalizer._remove_accents("ã"), "a")

    def test_accents_tilde_o(self):
        self.assertEqual(self.normalizer._remove_accents("õ"), "o")

    def test_accents_tilde_all(self):
        self.assertEqual(self.normalizer._remove_accents("ãõ"), "ao")

    # Diaeresis / umlaut
    def test_accents_dieresis_a(self):
        self.assertEqual(self.normalizer._remove_accents("ä"), "a")

    def test_accents_dieresis_e(self):
        self.assertEqual(self.normalizer._remove_accents("ë"), "e")

    def test_accents_dieresis_i(self):
        self.assertEqual(self.normalizer._remove_accents("ï"), "i")

    def test_accents_dieresis_o(self):
        self.assertEqual(self.normalizer._remove_accents("ö"), "o")

    def test_accents_dieresis_u(self):
        self.assertEqual(self.normalizer._remove_accents("ü"), "u")

    def test_accents_dieresis_all_vowels(self):
        self.assertEqual(self.normalizer._remove_accents("äëïöü"), "aeiou")

    # Ring
    def test_accents_ring_a(self):
        self.assertEqual(self.normalizer._remove_accents("å"), "a")

    def test_accents_ring_u(self):
        self.assertEqual(self.normalizer._remove_accents("ů"), "u")

    # Cedilla
    def test_accents_cedilla_c(self):
        self.assertEqual(self.normalizer._remove_accents("ç"), "c")

    # Caron
    def test_accents_caron_c(self):
        self.assertEqual(self.normalizer._remove_accents("č"), "c")

    def test_accents_caron_s(self):
        self.assertEqual(self.normalizer._remove_accents("š"), "s")

    def test_accents_caron_z(self):
        self.assertEqual(self.normalizer._remove_accents("ž"), "z")

    def test_accents_caron_all(self):
        self.assertEqual(self.normalizer._remove_accents("čšž"), "csz")

    # Stroke
    def test_accents_stroke_o(self):
        self.assertEqual(self.normalizer._remove_accents("ø"), "o")

    def test_accents_stroke_l(self):
        self.assertEqual(self.normalizer._remove_accents("ł"), "l")

    def test_accents_stroke_d(self):
        self.assertEqual(self.normalizer._remove_accents("đ"), "d")

    # Macron
    def test_accents_macron_a(self):
        self.assertEqual(self.normalizer._remove_accents("ā"), "a")

    def test_accents_macron_e(self):
        self.assertEqual(self.normalizer._remove_accents("ē"), "e")

    def test_accents_macron_i(self):
        self.assertEqual(self.normalizer._remove_accents("ī"), "i")

    def test_accents_macron_o(self):
        self.assertEqual(self.normalizer._remove_accents("ō"), "o")

    def test_accents_macron_u(self):
        self.assertEqual(self.normalizer._remove_accents("ū"), "u")

    def test_accents_macron_all_vowels(self):
        self.assertEqual(self.normalizer._remove_accents("āēīōū"), "aeiou")

    # Ogonek
    def test_accents_ogonek_a(self):
        self.assertEqual(self.normalizer._remove_accents("ą"), "a")

    def test_accents_ogonek_e(self):
        self.assertEqual(self.normalizer._remove_accents("ę"), "e")

    def test_accents_ogonek_i(self):
        self.assertEqual(self.normalizer._remove_accents("į"), "i")

    def test_accents_ogonek_u(self):
        self.assertEqual(self.normalizer._remove_accents("ų"), "u")

    # No accent
    def test_accents_no_accent_unchanged(self):
        self.assertEqual(self.normalizer._remove_accents("abcdef"), "abcdef")

    def test_accents_numbers_unchanged(self):
        self.assertEqual(self.normalizer._remove_accents("áéíóú123"), "aeiou123")

    def test_accents_empty_string(self):
        self.assertEqual(self.normalizer._remove_accents(""), "")

    # Words in different languages
    def test_accents_portuguese(self):
        self.assertEqual(
            self.normalizer._remove_accents("não ações coração"),
            "nao acoes coracao"
        )

    def test_accents_spanish(self):
        self.assertEqual(
            self.normalizer._remove_accents("mañana niño corazón"),
            "manana nino corazon"
        )

    def test_accents_french(self):
        self.assertEqual(
            self.normalizer._remove_accents("élève déjà où"),
            "eleve deja ou"
        )

    def test_accents_german(self):
        self.assertEqual(
            self.normalizer._remove_accents("Fräulein schön über"),
            "Fraulein schon uber"
        )

    # ============================================================
    # _normalize_whitespace
    # ============================================================
    def test_whitespace_multiple_spaces(self):
        self.assertEqual(
            self.normalizer._normalize_whitespace("hello    world"),
            "hello world"
        )

    def test_whitespace_tabs(self):
        self.assertEqual(
            self.normalizer._normalize_whitespace("hello\t\tworld"),
            "hello world"
        )

    def test_whitespace_mixed_spaces_and_tabs(self):
        self.assertEqual(
            self.normalizer._normalize_whitespace("hello \t   world"),
            "hello world"
        )

    def test_whitespace_leading_spaces(self):
        self.assertEqual(
            self.normalizer._normalize_whitespace("   hello world"),
            "hello world"
        )

    def test_whitespace_trailing_spaces(self):
        self.assertEqual(
            self.normalizer._normalize_whitespace("hello world   "),
            "hello world"
        )

    def test_whitespace_leading_and_trailing(self):
        self.assertEqual(
            self.normalizer._normalize_whitespace("   hello world   "),
            "hello world"
        )

    def test_whitespace_preserves_paragraphs(self):
        result = self.normalizer._normalize_whitespace(
            "hello    world\n\n   how are    you"
        )
        self.assertEqual(result, "hello world\n\nhow are you")

    def test_whitespace_multiple_paragraphs(self):
        result = self.normalizer._normalize_whitespace(
            "first   paragraph\n\n\n\nsecond    paragraph"
        )
        self.assertEqual(result, "first paragraph\n\n\n\nsecond paragraph")

    def test_whitespace_only_spaces(self):
        self.assertEqual(
            self.normalizer._normalize_whitespace("     "),
            ""
        )

    def test_whitespace_only_newlines(self):
        self.assertEqual(
            self.normalizer._normalize_whitespace("\n\n\n"),
            "\n\n\n"
        )

    def test_whitespace_empty_string(self):
        self.assertEqual(self.normalizer._normalize_whitespace(""), "")

    # ============================================================
    # _normalize_punctuation_spacing
    # ============================================================
    def test_punctuation_comma_word_right(self):
        self.assertEqual(
            self.normalizer._normalize_punctuation_spacing("hello,world"),
            "hello , world"
        )

    def test_punctuation_comma_word_left(self):
        self.assertEqual(
            self.normalizer._normalize_punctuation_spacing("hello,world"),
            "hello , world"
        )

    def test_punctuation_period(self):
        self.assertEqual(
            self.normalizer._normalize_punctuation_spacing("hello.world"),
            "hello . world"
        )

    def test_punctuation_exclamation(self):
        self.assertEqual(
            self.normalizer._normalize_punctuation_spacing("hello!world"),
            "hello ! world"
        )

    def test_punctuation_question(self):
        self.assertEqual(
            self.normalizer._normalize_punctuation_spacing("hello?world"),
            "hello ? world"
        )

    def test_punctuation_semicolon(self):
        self.assertEqual(
            self.normalizer._normalize_punctuation_spacing("hello;world"),
            "hello ; world"
        )

    def test_punctuation_colon(self):
        self.assertEqual(
            self.normalizer._normalize_punctuation_spacing("hello:world"),
            "hello : world"
        )

    def test_punctuation_word_then_punctuation(self):
        self.assertEqual(
            self.normalizer._normalize_punctuation_spacing("hi,"),
            "hi ,"
        )

    def test_punctuation_punctuation_then_word(self):
        self.assertEqual(
            self.normalizer._normalize_punctuation_spacing(",hi"),
            ", hi"
        )

    def test_punctuation_multiple_in_sentence(self):
        self.assertEqual(
            self.normalizer._normalize_punctuation_spacing("hi,how are you?fine;thanks."),
            "hi , how are you ? fine ; thanks ."
        )

    def test_punctuation_already_spaced_unchanged(self):
        self.assertEqual(
            self.normalizer._normalize_punctuation_spacing("hi , how are you ?"),
            "hi , how are you ?"
        )

    def test_punctuation_numbers_unchanged(self):
        self.assertEqual(
            self.normalizer._normalize_punctuation_spacing("123,456.78"),
            "123,456.78"
        )

    def test_punctuation_only_marks(self):
        self.assertEqual(
            self.normalizer._normalize_punctuation_spacing(".,!?;:"),
            ".,!?;:"
        )

    def test_punctuation_empty_string(self):
        self.assertEqual(
            self.normalizer._normalize_punctuation_spacing(""),
            ""
        )

    # ============================================================
    # normalize (full pipeline)
    # ============================================================
    def test_normalize_all_transformations(self):
        result = self.normalizer.normalize("Café,  por favor!   Está   Pronto?")
        self.assertEqual(result, "cafe , por favor ! esta pronto ?")

    def test_normalize_multiline_with_accents_and_punctuation(self):
        result = self.normalizer.normalize("Olá,    tudo bem?\n\n   Estou   Ótimo!")
        self.assertEqual(result, "ola , tudo bem ?\n\nestou otimo !")

    def test_normalize_no_changes_needed(self):
        text = "hello world"
        self.assertEqual(self.normalizer.normalize(text), "hello world")

    def test_normalize_only_accents(self):
        result = self.normalizer.normalize("café mañana piñata")
        self.assertEqual(result, "cafe manana pinata")

    def test_normalize_only_whitespace(self):
        result = self.normalizer.normalize("hello   world\t\ttest")
        self.assertEqual(result, "hello world test")

    def test_normalize_only_punctuation(self):
        result = self.normalizer.normalize("hi,hello!how?")
        self.assertEqual(result, "hi , hello ! how ?")

    def test_normalize_empty_string(self):
        self.assertEqual(self.normalizer.normalize(""), "")

    def test_normalize_very_long_string(self):
        text = "Café   com  pão?  " * 1000
        expected = "cafe com pao ? " * 1000
        expected = expected.strip()
        result = self.normalizer.normalize(text)
        self.assertEqual(result, expected)