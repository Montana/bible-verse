#!/usr/bin/env python3

import random

VERSES = [
    ("Genesis 1:1", "In the beginning God created the heaven and the earth."),
    ("Psalm 23:1", "The LORD is my shepherd; I shall not want."),
    ("Psalm 23:4", "Yea, though I walk through the valley of the shadow of death, I will fear no evil: for thou art with me; thy rod and thy staff they comfort me."),
    ("Psalm 46:10", "Be still, and know that I am God: I will be exalted among the heathen, I will be exalted in the earth."),
    ("Psalm 119:105", "Thy word is a lamp unto my feet, and a light unto my path."),
    ("Psalm 139:14", "I will praise thee; for I am fearfully and wonderfully made: marvellous are thy works; and that my soul knoweth right well."),
    ("Proverbs 3:5-6", "Trust in the LORD with all thine heart; and lean not unto thine own understanding. In all thy ways acknowledge him, and he shall direct thy paths."),
    ("Proverbs 18:10", "The name of the LORD is a strong tower: the righteous runneth into it, and is safe."),
    ("Isaiah 40:31", "But they that wait upon the LORD shall renew their strength; they shall mount up with wings as eagles; they shall run, and not be weary; and they shall walk, and not faint."),
    ("Isaiah 41:10", "Fear thou not; for I am with thee: be not dismayed; for I am thy God: I will strengthen thee; yea, I will help thee; yea, I will uphold thee with the right hand of my righteousness."),
    ("Jeremiah 29:11", "For I know the thoughts that I think toward you, saith the LORD, thoughts of peace, and not of evil, to give you an expected end."),
    ("Matthew 5:16", "Let your light so shine before men, that they may see your good works, and glorify your Father which is in heaven."),
    ("Matthew 6:33", "But seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you."),
    ("Matthew 11:28", "Come unto me, all ye that labour and are heavy laden, and I will give you rest."),
    ("Matthew 28:20", "Teaching them to observe all things whatsoever I have commanded you: and, lo, I am with you always, even unto the end of the world."),
    ("John 1:1", "In the beginning was the Word, and the Word was with God, and the Word was God."),
    ("John 3:16", "For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life."),
    ("John 8:32", "And ye shall know the truth, and the truth shall make you free."),
    ("John 14:6", "Jesus saith unto him, I am the way, the truth, and the life: no man cometh unto the Father, but by me."),
    ("John 14:27", "Peace I leave with you, my peace I give unto you: not as the world giveth, give I unto you. Let not your heart be troubled, neither let it be afraid."),
    ("John 16:33", "These things I have spoken unto you, that in me ye might have peace. In the world ye shall have tribulation: but be of good cheer; I have overcome the world."),
    ("Romans 5:8", "But God commendeth his love toward us, in that, while we were yet sinners, Christ died for us."),
    ("Romans 8:28", "And we know that all things work together for good to them that love God, to them who are the called according to his purpose."),
    ("Romans 8:38-39", "For I am persuaded, that neither death, nor life, nor angels, nor principalities, nor powers, nor things present, nor things to come, nor height, nor depth, nor any other creature, shall be able to separate us from the love of God, which is in Christ Jesus our Lord."),
    ("Romans 12:2", "And be not conformed to this world: but be ye transformed by the renewing of your mind, that ye may prove what is that good, and acceptable, and perfect, will of God."),
    ("1 Corinthians 10:13", "There hath no temptation taken you but such as is common to man: but God is faithful, who will not suffer you to be tempted above that ye are able; but will with the temptation also make a way to escape, that ye may be able to bear it."),
    ("1 Corinthians 13:4-5", "Charity suffereth long, and is kind; charity envieth not; charity vaunteth not itself, is not puffed up, doth not behave itself unseemly, seeketh not her own, is not easily provoked, thinketh no evil."),
    ("2 Corinthians 5:17", "Therefore if any man be in Christ, he is a new creature: old things are passed away; behold, all things are become new."),
    ("2 Corinthians 12:9", "And he said unto me, My grace is sufficient for thee: for my strength is made perfect in weakness."),
    ("Galatians 5:22-23", "But the fruit of the Spirit is love, joy, peace, longsuffering, gentleness, goodness, faith, meekness, temperance: against such there is no law."),
    ("Ephesians 2:8-9", "For by grace are ye saved through faith; and that not of yourselves: it is the gift of God: not of works, lest any man should boast."),
    ("Ephesians 6:10", "Finally, my brethren, be strong in the Lord, and in the power of his might."),
    ("Philippians 4:6-7", "Be careful for nothing; but in every thing by prayer and supplication with thanksgiving let your requests be made known unto God. And the peace of God, which passeth all understanding, shall keep your hearts and minds through Christ Jesus."),
    ("Philippians 4:13", "I can do all things through Christ which strengtheneth me."),
    ("Colossians 3:23", "And whatsoever ye do, do it heartily, as to the Lord, and not unto men."),
    ("2 Timothy 1:7", "For God hath not given us the spirit of fear; but of power, and of love, and of a sound mind."),
    ("Hebrews 11:1", "Now faith is the substance of things hoped for, the evidence of things not seen."),
    ("Hebrews 13:8", "Jesus Christ the same yesterday, and to day, and for ever."),
    ("James 1:5", "If any of you lack wisdom, let him ask of God, that giveth to all men liberally, and upbraideth not; and it shall be given him."),
    ("1 Peter 5:7", "Casting all your care upon him; for he careth for you."),
    ("1 John 4:19", "We love him, because he first loved us."),
    ("Revelation 21:4", "And God shall wipe away all tears from their eyes; and there shall be no more death, neither sorrow, nor crying, neither shall there be any more pain: for the former things are passed away."),
]


def main():
    ref, text = random.choice(VERSES)
    print(f"\n  📖 {ref}\n")
    print(f"  \"{text}\"\n")


if __name__ == "__main__":
    main()
