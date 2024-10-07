# rules.py
from production import IF, AND, OR, THEN, NOT

TOURIST_RULES = (
    IF(AND('(?x) has blue skin'),
       THEN('(?x) is a Loonie!')),

    IF(OR('(?x) has white skin', '(?x) has yellow skin','(?x) has black skin'),
       THEN('(?x) is a general_tourist')),

    IF(
        AND(
            '(?x) is a general_tourist',
            OR(
                '(?x) dressed in classic attire',
                AND('(?x) dressed in smart casual attire', '(?x) travels by expensive car')
            )
        ),
        THEN('(?x) is a wealthy_tourist')
    ),

    IF(
        AND(
            '(?x) is a wealthy_tourist',
            OR('(?x) has a precise and formal speech', '(?x) has interest in business conferences')
        ),
        THEN('(?x) is a Business traveller!')
    ),
    IF(
        AND(
            '(?x) is a wealthy_tourist',
            OR('(?x) has an elegant and well-articulated speech', '(?x) has interest in shopping')
        ),
        THEN('(?x) is a Luxury traveller!')
    ),

    IF(
        AND(
            '(?x) is a general_tourist',
            OR(
                AND(
                    '(?x) dressed in simple casual attire',
                    OR('(?x) travels by bicycle', '(?x) travels by foot')
                ),
                '(?x) dressed in sport attire'
            ),
        ),
        THEN('(?x) is a healthy_lifestyle_enthusiast')
    ),

    IF(
        AND(
            OR(
                '(?x) is a healthy_lifestyle_enthusiast',
                '(?x) travels by public transport',
                '(?x) travels by car',
            ),
            '(?x) has interest in learning/research'
        ),
        THEN('(?x) is a Student traveller!')
    ),
    IF(
        AND(
            '(?x) is a healthy_lifestyle_enthusiast',
            '(?x) has interest in national parks and natural reserves'
        ),
        THEN('(?x) is a Adventure Traveller!')
    ),

    IF(
        AND(
            '(?x) is a general_tourist',
            AND(
                OR(
                    '(?x) dressed in simple casual attire',
                    '(?x) travels by public transport',
                    '(?x) travels by car',
                ),
                OR('(?x) with children', '(?x) with spouse', '(?x) with children and spouse')
            ),
        ),
        THEN('(?x) is a Family traveller!')
    ),
    IF(
        AND(
            '(?x) is a healthy_lifestyle_enthusiast',
            '(?x) has interest in national parks and natural reserves'
        ),
        THEN('(?x) is a Adventure Traveller!')
    ),
)
