from rest_framework import serializers
from currency.models import Currency
from utils.helper import (
    float_int_extraction,
    fraction_to_words, generate_segments,
    input_sanitizer,
    whole_part_word_gen
)


class CurrencySerializer(serializers.ModelSerializer):
    """
    Currency Serializer
    """
    convert_bangla = serializers.SerializerMethodField('english_bangla')

    def english_bangla(self, obj):
        number = input_sanitizer(obj.value)
        whole, fraction = float_int_extraction(number)
        whole_segments = generate_segments(whole)
        generated_words = whole_part_word_gen(whole_segments)
        if fraction:
            if generated_words:
                return generated_words + " দশমিক " + fraction_to_words(fraction)
            else:
                return "দশমিক " + fraction_to_words(fraction)
        else:
            return generated_words

    class Meta(object):
        model = Currency
        fields = ['id', 'name', 'value', 'convert_bangla', 'created_at', 'updated_at']
