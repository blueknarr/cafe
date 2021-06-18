import os

from pymongo import MongoClient
from flask.cli import load_dotenv

load_dotenv()
MONGODB_HOST = os.environ['MONGODB_HOST']
db = None
client = MongoClient(MONGODB_HOST)
db = client.get_database('cafe')

hongdae = [
    {
        "title": "1984",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20161231_63%2F1483183304319WQnCF_JPEG%2F177181605163301_0.jpeg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20161231_214%2F1483183304556q0vEn_JPEG%2F177181605163301_1.jpeg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20161231_28%2F1483183304808Sb8hF_JPEG%2F177181605163301_2.jpeg",
        ],
        "theme": "아늑한",
        "tel": "02-325-1984",
        "address": "서울 마포구 동교로 194 혜원빌딩 1층",
        "location": "홍대",
        "open": "매일 10:00 - 24:00",
        "convenience": "단체석, 주차, 포장, 배달, 예약, 무선 인터넷",
        "insta": "http://instagram.com/1984store",
        "menu": [
            {
                "name": "에스프레소",
                "price": "5,000원"
            },
            {
                "name": "아메리카노",
                "price": "5,500원"
            },
            {
                "name": "카페라떼",
                "price": "6,000원"
            },
            {
                "name": "카푸치노",
                "price": "6,000원"
            }
        ],
        "review": [
            {
                "user": "GGIL",
                "content": "음료는 비싼데 맛있네요 스테피바이스 엄청 맛있는 맥주네요",
                "date": "2021.06.05",
                "rating": "5"
            }
        ]
    },
    {
        "title": "꽈페",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20201229_57%2F1609236830710rQhKx_JPEG%2FP3zNZpkXGtu5AwE832KkjPQ2.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20201229_62%2F1609236829849RqM2G_JPEG%2FRSAXi0yDUq6J-a0C1lCQf-xA.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20201229_200%2F16092368308494mHIJ_JPEG%2FF-HQLUwYa_hX9Rgs638dPh2N.jpg"
        ],
        "theme": "편안한 분위기",
        "tel": "02-332-7567",
        "address": "서울 마포구 동교로46길 20 1층",
        "location": "홍대",
        "open": "매일 10:30 - 22:00",
        "insta": "https://www.instagram.com/quafe_twisted",
        "convenience": "포장, 무선 인터넷, 반려동물 동반, 제로페이",
        "menu": [
            {
                "name": "유니콘 트위스트",
                "price": "2,500원"
            },
            {
                "name": "카야코코넛 트위스트",
                "price": "2,900원"
            },
            {
                "name": "시나몬 트위스트",
                "price": "1,800원"
            },
            {
                "name": "아메리카노",
                "price": "4,500원"
            }
        ],
        "review": [
            {
                "user": "prettycreat",
                "content": "일반적인 꽈베기 맛이 아니에요 묘하게 맛있네요",
                "date": "2021.06.09",
                "rating": "4"
            }
        ]
    },
    {
        "title": "샌드커피 논탄토",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20180801_238%2F1533107192129iO6eX_JPEG%2FFBZ_0dbJzz9GWsp9nMvfeLeb.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20180801_175%2F1533107198388xlsde_JPEG%2Fey6eUs8B_nZ38ZgLFA-mNFTn.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20180801_297%2F1533107206593PFMpS_JPEG%2Fj7pStWHKErUOF8y2LWOTTg0Y.jpg"
        ],
        "theme": "분위기있는",
        "tel": "02-336-8020",
        "address": "서울 마포구 동교로 212-16",
        "location": "홍대",
        "open": "매일 11:00 - 23:00",
        "insta": "https://www.instagram.com/nontanto_sandcoffee/",
        "convenience": "단체석, 주차, 포장, 무선 인터넷, 반려동물 동반",
        "menu": [
            {
                "name": "체즈베",
                "price": "4,500원"
            },
            {
                "name": "골든 크림 라떼",
                "price": "6,500원"
            },
            {
                "name": "쿠네페",
                "price": "8,500원"
            }
        ],
        "review": [
            {
                "user": "kej",
                "content": "터키에서 먹던 맛이네요. 너무 부드러워요",
                "date": "2021.06.07",
                "rating": "5"
            }
        ]
    },
    {
        "title": "코코로카라",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20171121_178%2F1511213538308aOsLw_JPEG%2FWyMke57zs20VdHjAwkRvZKdy.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20171121_245%2F1511213538430uT0k5_JPEG%2FF6UsxboHkwbjKgY2tINARCgZ.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20171121_51%2F1511213709074ykUeX_JPEG%2FChGigi-MVSsmiGd8_CjxgPaR.jpg"
        ],
        "theme": "작업하기좋은",
        "tel": "070-8829-0088",
        "address": "서울 마포구 월드컵북로8길 17",
        "location": "홍대",
        "open": "매일 12:00 - 20:00",
        "insta": "https://www.instagram.com/_kokorokara_/",
        "convenience": "주차, 포장, 제로페이",
        "menu": [
            {
                "name": "바나나푸딩",
                "price": "6,900원"
            },
            {
                "name": "브루키",
                "price": "4,200원"
            },
            {
                "name": "쿠키류",
                "price": "2,300원"
            },
            {
                "name": "구움 케익류",
                "price": "3,600원"
            }
        ],
        "review": [
            {
                "user": "빵순이",
                "content": "줄이 짱짱 길지만 푸딩 겟했습니자!",
                "date": "2021.06.05",
                "rating": "4.5"
            }
        ]
    },
    {
        "title": "펠른",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200429_169%2F1588158068752uUOho_JPEG%2FAT_Perlen_Spaces11_%25BF%25EB%25B7%25AE%25C1%25D9%25C0%25D3.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200429_292%2F15881580686046K0EX_JPEG%2FAT_Perlen_Spaces3_%25BF%25EB%25B7%25AE%25C1%25D9%25C0%25D3.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200420_118%2F1587367241807eib4G_JPEG%2FjqjGxZHqj2aNEAxUj04gGkSz.jpg"
        ],
        "theme": "아늑한",
        "tel": "02-332-9287",
        "address": "서울 마포구 성미산로22길 18 A'동 1층 펠른",
        "location": "홍대",
        "open": "매일 12:00 - 21:00 설날, 추석 당일 휴무",
        "insta": "http://www.instagram.com/perlen_official/",
        "convenience": "주차, 포장, 예약, 무선 인터넷, 남/녀 화장실 구분",
        "menu": [
            {
                "name": "펠른 페어링 코스",
                "price": "38,000원"
            },
            {
                "name": "위스키 더치",
                "price": "8,500원"
            },
            {
                "name": "펠른 도스",
                "price": "8,000원"
            },
            {
                "name": "과일 (커피)",
                "price": "7,000원"
            }
        ],
        "review": [
            {
                "user": "spspq2",
                "content": "분위기랑 디저트 좋았습니다",
                "date": "2021.06.05",
                "rating": "4"
            }
        ]
    },
    {
        "title": "카페 장쌤",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20170818_60%2F1503022540754dbQUW_JPEG%2F8BK-GXuQv2b7rx9s9Sh7Pax2.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA1MTRfOTAg%2FMDAxNjIxMDAwNDE0MDM5.Zt2r4dVbnGxL1F3S6ln511yVerPp5onuUYd945D_HgMg.GB59Ds--2P2SwbDIBByU-KhKOeqYOjHqAD5JQb9hbqEg.JPEG.syy404%2FIMG_1632.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA1MzBfMTg1%2FMDAxNjIyMzU4ODEwNzI0.ZFw6xU_JJetm0PwZRsqeyz-co0ngqDeEowNu7dF2AjEg.5QN6H9KCo1KRjPLFtCSfe3RyYABXSScleiQrguys26gg.JPEG.graynpink%2FIMG_3830.jpg"
        ],
        "theme": "편안한 분위기",
        "tel": "070-4084-3414",
        "address": "서울 마포구 와우산로29마길 5",
        "location": "홍대",
        "open": "매일 12:00 - 21:00",
        "insta": "https://www.instagram.com/jangssamcafe/",
        "convenience": "포장, 예약",
        "menu": [
            {
                "name": "생생오렌지에이드",
                "price": "6,500원"
            },
            {
                "name": "생생레몬에이드",
                "price": "6,000원"
            },
            {
                "name": "산딸기에이드",
                "price": "6,500원"
            }
        ],
        "review": [
            {
                "user": "qlw",
                "content": "존맛탱!!",
                "date": "2021.05.29",
                "rating": "4.5"
            }
        ]
    },
    {
        "title": "사월의물고기",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200821_211%2F1597972947092qGbCQ_JPEG%2FRlMoHKrzWUpxbafQ4IF_6b4f.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200821_276%2F15979728743389GJ4C_JPEG%2FIVSq6ZdXHCmR9fV4_O75apkM.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200822_8%2F1598077079405WspOF_JPEG%2FKakaoTalk_20200820_194626215.jpg"
        ],
        "theme": "분위기있는",
        "tel": "0507-1405-3117",
        "address": "서울 마포구 성미산로 89 1층",
        "location": "홍대",
        "open": "매일 12:30 - 20:30",
        "insta": "https://smartstore.naver.com/4wall_fish/category/50000006?cp=1",
        "convenience": "포장, 무선 인터넷",
        "menu": [
            {
                "name": "쑥글레이즈 스콘",
                "price": "3,800원"
            },
            {
                "name": "크리스피 에타(Egg Tart)",
                "price": "3,000원"
            },
            {
                "name": "바싹 크리스피 에타 4개 세트",
                "price": "10,000원"
            },
            {
                "name": "쑥비엔나",
                "price": "5,800원"
            }
        ],
        "review": [
            {
                "user": "dkf",
                "content": "오 맛있어요!!!!!!! 타르트 넘 달아여 ㅋㅋㅋㅋ 맛있어용",
                "date": "2021.05.30",
                "rating": "5"
            }
        ]
    },
    {
        "title": "Deweet",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200511_195%2F1589181622104agcsk_JPEG%2Ft3EUSmnl4-E0SiyC_JGbRwUO.jpeg.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200511_261%2F1589181642497iB1oK_JPEG%2FsvaJEL4dr4w9JkrKr-305EYx.jpeg.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200511_267%2F15891816664039E4a0_JPEG%2FcQ00UdIQ8P0De9SG6PYXuC1W.jpeg.jpg"
        ],
        "theme": "작업하기좋은",
        "tel": "0507-1440-2037",
        "address": "서울 마포구 동교로 242-5",
        "location": "홍대",
        "open": "매일 12:00 - 23:00",
        "insta": "https://www.instagram.com/cafedeweet/",
        "convenience": "포장, 예약, 무선 인터넷",
        "menu": [
            {
                "name": "프레지에",
                "price": "6,700원"
            },
            {
                "name": "피귀에",
                "price": "7,200원"
            },
            {
                "name": "아메리카노",
                "price": "5,000원"
            },
            {
                "name": "마카롱",
                "price": "2,300원"
            }
        ],
        "review": [
            {
                "user": "데굴떼굴",
                "content": "케이크 너무 맛있어요~",
                "date": "2021.06.05",
                "rating": "5"
            }
        ]
    },
    {
        "title": "카페요호",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200619_29%2F1592556047346V0tgA_JPEG%2F0X3SDnTvaJVE1FIAzVZw9GMe.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200619_95%2F1592556047069sxFIu_JPEG%2F4FxeGI5sFmfx87bMx_4p27XI.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200619_2%2F15925560469231xzXu_JPEG%2FhliNHBw6McQvylT6HZNcCRRK.jpg"
        ],
        "theme": "아늑한",
        "tel": "02-336-0150",
        "address": "서울 마포구 잔다리로 88 원방빌딩 1F",
        "location": "홍대",
        "open": "매일 11:00 - 19:00",
        "insta": "https://www.instagram.com/cafeyoho/",
        "convenience": "단체석, 주차, 포장, 배달, 무선 인터넷, 남/녀 화장실 구분",
        "menu": [
            {
                "name": "스무디 볼",
                "price": "8,000원"
            },
            {
                "name": "빅-빅 브런치 콤보",
                "price": "39,000원"
            },
            {
                "name": "아메리카노",
                "price": "4,500원"
            },
            {
                "name": "카페라떼",
                "price": "5,000원"
            }
        ],
        "review": [
            {
                "user": "찌니",
                "content": "직원분들도 엄청 착하시고 라떼가 정말 맛있어요!!",
                "date": "2021.03.09",
                "rating": "5"
            }
        ]
    },
    {
        "title": "Are&am",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20201129_117%2F1606655261408YGMfv_JPEG%2FTi9ghqm1xfo4WJYSVjj7enes.jpeg.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210228_99%2F1614441048069vJnFQ_JPEG%2Fu7DIrPnZzy8-dOGmH6TVZ1oz.jpeg.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20201129_77%2F1606655307427dtMhj_JPEG%2FyYQMkxJTYIFyTmCRTjVTbqe-.jpeg.jpg"
        ],
        "theme": "편안한 분위기",
        "tel": "0507-1335-0910",
        "address": "서울 마포구 성미산로17길 12 1층",
        "location": "홍대",
        "open": "매일 12:00 - 20:30",
        "insta": "http://www.instagram.com/are.and.am",
        "convenience": "포장, 무선 인터넷, 제로페이",
        "menu": [
            {
                "name": "딸기 초콜릿 수프",
                "price": "6,500원"
            },
            {
                "name": "딸기 초콜릿 티라미수",
                "price": "9,500원"
            },
            {
                "name": "다크 핑크 모카",
                "price": "6,500원"
            },
            {
                "name": "초콜릿 크로플",
                "price": "8,000원"
            }
        ],
        "review": [
            {
                "user": "파란심바",
                "content": "다쿠아즈도 맛나고 밀크티도 맛나고 시그니처커피들은 비주얼부터 즐거워요",
                "date": "2021.05.26",
                "rating": "5"
            }
        ]
    },
    {
        "title": "카페 사운드웨이브",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200319_119%2F1584609490531JGBPA_JPEG%2FegaCUj0LZdWOUaguPIAlMLw6.jpeg.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200319_184%2F1584609263698Q6g8k_JPEG%2FQHGb2zOo_Pxl6L4tBwHjgU2z.jpeg.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200319_137%2F1584609264010fnMBQ_JPEG%2FD5PAk8zgoyC4elA6j6caHJDN.jpeg.jpg"
        ],
        "theme": "분위기있는",
        "tel": "0507-1342-3758",
        "address": "서울 마포구 독막로3길 24 3층",
        "location": "상수",
        "open": "매일 11:00 - 20:00",
        "insta": "http://www.instagram.com/cafesoundwave",
        "convenience": "단체석, 포장, 무선 인터넷, 남/녀 화장실 구분",
        "menu": [
            {
                "name": "애플유자티",
                "price": "6,500원"
            },
            {
                "name": "아메리카노",
                "price": "3,500"
            },
            {
                "name": "딸기라테",
                "price": "4,500원"
            },
            {
                "name": "카페라떼",
                "price": "4,000원"
            }
        ],
        "review": [
            {
                "user": "CIEL",
                "content": "너무너무 친절하세요. 근데 일처리가 좀 느리신 듯.",
                "date": "2021.06.01",
                "rating": "4.5"
            }
        ]
    },
    {
        "title": "카페 마로스",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20191029_173%2F1572329237694MXBkh_JPEG%2F6HOh7Htj9i80NTKp_xJ2P72r.jpeg.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210101_60%2F1609470458415ikRrc_JPEG%2FO4_z0V7A7dHSQ4yGww7tMCXx.jpeg.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210101_271%2F1609470579214VfysU_JPEG%2FahO6Yu3LYS-P8Xvf6qVCcmmm.jpeg.jpg"
        ],
        "theme": "작업하기좋은",
        "tel": "02-336-0428",
        "address": "서울 마포구 양화로6길 86 1층",
        "location": "상수",
        "open": "매일 13:00 - 21:00",
        "insta": "https://instagram.com/cafe_maros",
        "convenience": "포장, 무선 인터넷, 반려동물 동반, 제로페이",
        "menu": [
            {
                "name": "스모어쿠키",
                "price": "3,900원"
            },
            {
                "name": "쿠키류",
                "price": "3,900원"
            }
        ],
        "review": [
            {
                "user": "enqn326",
                "content": "쿠키 진짜 맛있고 사장님 짱 친절하세용",
                "date": "2021.06.09",
                "rating": "5"
            }
        ]
    },
    {
        "title": "어반플랜트",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20171023_126%2F1508733221550wYRXp_JPEG%2FqDGDXzl4x3imgb_E3GECNae-.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20171023_75%2F1508733221605JFbBj_JPEG%2FJKkbt1QJR8LQJgR9osoKep-P.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20180613_173%2F1528824895634DiRgU_JPEG%2Fk9LxIobZlKb5-FjlmsQRNh5d.jpeg.jpg"
        ],
        "theme": "아늑한",
        "tel": "0507-1413-0378",
        "address": "서울 마포구 독막로4길 3",
        "location": "상수",
        "open": "매일 10:00 - 23:00",
        "insta": "https://www.instagram.com/cafe_urbanplant/",
        "convenience": "단체석, 포장, 무선 인터넷",
        "menu": [
            {
                "name": "URBAN Caesar",
                "price": "14,000원"
            },
            {
                "name": "Special Caprese",
                "price": "13,800원"
            },
            {
                "name": "Cheese Avocado Omelet",
                "price": "14,300원"
            },
            {
                "name": "Signature Omelet",
                "price": "14,300원"
            }
        ],
        "review": [
            {
                "user": "yeo",
                "content": "초록초록 음식도 맛나구 양도 많늠",
                "date": "2021.02.26",
                "rating": "5"
            }
        ]
    },
    {
        "title": "OSECHILL",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200331_6%2F1585585709393owRgb_JPEG%2FTG9u4g7D3EPUg3WHt5aoEkli.jpeg.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20201111_276%2F1605089043123DblUH_JPEG%2FQLJwU88xRh0Gm3zDHd1nmjjC.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200331_36%2F15855856843966Ev6g_JPEG%2FOA2yEUkHm76Swo7u3xNNgCof.jpeg.jpg"
        ],
        "theme": "편안한 분위기",
        "tel": "02-322-1543",
        "address": "서울 마포구 토정로5길 17 1층",
        "location": "",
        "open": "매일 11:00 - 20:00",
        "insta": "http://instagram.com/osechill_cafe",
        "convenience": "무선 인터넷, 남/녀 화장실 구분",
        "menu": [
            {
                "name": "Americano",
                "price": "5,000원"
            },
            {
                "name": "카페라떼",
                "price": "5,500원"
            },
            {
                "name": "카푸치노",
                "price": "5,500원"
            },
            {
                "name": "초콜릿라떼",
                "price": "5,500원"
            }
        ],
        "review": [
            {
                "user": "",
                "content": "",
                "date": "",
                "rating": ""
            }
        ]
    },
    {
        "title": "봇봇봇",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200807_254%2F1596787316117cEogI_PNG%2FKYM2b-q6QTiYhhvnDmS4aDrc.png",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200807_27%2F1596787312510eLCas_PNG%2FKwHKVF3VjoN-OXmxqZtAM82b.png",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200807_24%2F1596787312357H9mCW_PNG%2FD0u512YJLKc10MIHVTlYKJsj.png"
        ],
        "theme": "분위기있는",
        "tel": "0507-1322-9219",
        "address": "서울 성동구 아차산로9길 8",
        "location": "성수",
        "open": "매일 11:00 - 22:00",
        "insta": "http://www.instagram.com/_bot.bot.bot/",
        "convenience": "단체석, 포장, 무선 인터넷, 반려동물 동반, 남/녀 화장실 구분",
        "menu": [
            {
                "name": "로맨슈페너 BOT",
                "price": "6,500원"
            },
            {
                "name": "라임 모히또 BOT",
                "price": "9,000원"
            },
            {
                "name": "아이스 아메리카노",
                "price": "4,500원"
            },
            {
                "name": "트리플 치즈 크로와상",
                "price": "10,000원"
            }
        ],
        "review": [
            {
                "user": "범이",
                "content": "좋아요",
                "date": "2021.06.13",
                "rating": "5"
            }
        ]
    },
    {
        "title": "루디먼트",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190916_77%2F1568635034062e2vc8_JPEG%2FLh1zaccHkTNcLqLuG7HBkRKO.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190916_199%2F15686350461769vKhV_JPEG%2F7tjO4BOleYAljbHrqSPV9t1m.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190916_37%2F1568635075361dv72f_JPEG%2FkEcsO98ajE02ahE3kFh7XIbD.jpg"
        ],
        "theme": "작업하기좋은",
        "tel": "0507-1317-7158",
        "address": "서울 성동구 아차산로7길 15-8",
        "location": "성수",
        "open": "매일 08:00 - 22:00",
        "insta": "http://instagram.com/rudiment.kr",
        "convenience": "단체석, 포장, 배달, 무선 인터넷, 반려동물 동반",
        "menu": [
            {
                "name": "아메리카노",
                "price": "4,500원"
            }
        ],
        "review": [
            {
                "user": "navely",
                "content": "조용하고 좋아요",
                "date": "2021.06.07",
                "rating": "4.5"
            }
        ]
    },
    {
        "title": "LITE LANE",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210401_198%2F1617265507518bkn3s_JPEG%2FccWQFr8lVGUI0SJl1wPs3ODt.jpeg.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210401_109%2F16172655433447CjUe_JPEG%2FnR1iVwJ7FHB3Jy8OspWn1xPC.jpeg.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210401_119%2F1617265626737VdTpw_JPEG%2F-ijOeMcr6IV00-7UfKnFzsQk.jpeg.jpg"
        ],
        "theme": "아늑한",
        "tel": "02-2122-1233",
        "address": "서울 광진구 아차산로 200 커먼그라운드 3층 라이트레인",
        "location": "",
        "open": "매일 11:00 - 22:00",
        "insta": "https://instagram.com/lite.lane_official?igshid=1davt9uetu03s",
        "convenience": "단체석, 주차, 포장, 예약, 무선 인터넷, 반려동물 동반, 남/녀 화장실 구분",
        "menu": [
            {
                "name": "아메리카노",
                "price": "5,000원"
            },
            {
                "name": "카페라떼",
                "price": "5,500원"
            },
            {
                "name": "허브 오렌지자몽",
                "price": "6,000원"
            },
            {
                "name": "허브 레몬애플",
                "price": "6,000원"
            }
        ],
        "review": [
            {
                "user": "chl",
                "content": "좋아요",
                "date": "2021.06.05",
                "rating": "4.5"
            }
        ]
    },
    {
        "title": "텍스쳐성수",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200928_128%2F1601265594780UAI1I_JPEG%2FapVeXF0dFPkpa9TrgpXGa78D.JPG.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200928_163%2F1601265594661XJ6iu_JPEG%2F7Y2KFXYAm731i2tX11R579l6.JPG.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200928_200%2F1601265594571629Aj_JPEG%2F_DlCeOTV2_tnCsPKX0woT2ek.JPG.jpg"
        ],
        "theme": "편안한 분위기",
        "tel": "070-4197-2740",
        "address": "서울 성동구 서울숲2길 16-12 1층",
        "location": "성수",
        "open": "매일 11:00 - 20:00",
        "insta": "https://www.instagram.com/txture.seongsu/",
        "convenience": "단체석, 포장, 무선 인터넷",
        "menu": [
            {
                "name": "티라미수",
                "price": "7,500원"
            }
        ],
        "review": [
            {
                "user": "hyemin",
                "content": "커피도 맛있고 분위기 좋아요~!",
                "date": "2021.06.01",
                "rating": "5"
            }
        ]
    },
    {
        "title": "책다방 위숨",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20170209_199%2F14866149299217XNCS_JPEG%2F186158505663599_0.jpeg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20170209_83%2F148661492996487VD0_JPEG%2F186158505663599_1.jpeg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20181128_153%2F1543374262815gdaW7_JPEG%2FwLMyitCdqrcUCFeVt7I5PLQY.jpg"
        ],
        "theme": "작업하기좋은",
        "tel": "070-4147-1681",
        "address": "서울 서대문구 연세로9길 34-1 HJ 빌딩",
        "location": "신촌",
        "open": "매일 11:30 - 22:00",
        "insta": "http://instagram.com/visum_bookdabang",
        "convenience": "단체석, 무선 인터넷, 남/녀 화장실 구분, 제로페이",
        "menu": [
            {
                "name": "에스프레소",
                "price": "4,500원"
            },
            {
                "name": "아메리카노",
                "price": "4,500원"
            },
            {
                "name": "카페라떼",
                "price": "5,000원"
            },
            {
                "name": "카푸치노",
                "price": "5,000원"
            }
        ],
        "review": [
            {
                "user": "윰",
                "content": "좋아요 ㅎㅎ!! 사장님 너무 친절하세요 ㅎㅎ",
                "date": "2021.05.22",
                "rating": "5"
            }
        ]
    },
    {
        "title": "독수리다방",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA0MTZfMjYz%2FMDAxNjE4NTU0Mzk2OTkx.CqSZASM4a6NzIHBbywoJpbGGH4UC62ZBddRmAi04q_8g.fKZhOMRi0_tgw1jTS5Mmy0bzd7rpZLf9ZjyPQ39avKYg.JPEG.shinny818%2FIMG_0410.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA0MTVfMjkw%2FMDAxNjE4NDkzODczOTkx.i280Mw6_vZufT5b0ROY6or4nKM4uxIJbC9awbVbjHDIg.3pg3g4RwanKBUzeInlTu0Neji4TPAyNy0hAY6PXsxdAg.JPEG.mlifaw%2FKakaoTalk_20210415_221642020.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA2MDZfNDgg%2FMDAxNjIyOTYyODUxMDg1.mDEzDMZmcgMq8edMuRmD_CfzbqFxfFAYkqLiHWyL2Bcg.3PCVPZQQ8nMPBHK3wKRVJcYxkJvISwcRtQT4urFm7QUg.JPEG.skxakf1234%2Foutput_3510341580.jpg"
        ],
        "theme": "편안한 분위기",
        "tel": "02-363-1222",
        "address": "서울 서대문구 연세로 36 독수리빌딩 8층",
        "location": "신촌",
        "open": "평일 11:00 - 24:00",
        "insta": "http://www.facebook.com/pages/독수리다방/343714999069490?ref=hll",
        "convenience": "단체석, 포장, 예약, 무선 인터넷, 남/녀 화장실 구분",
        "menu": [
            {
                "name": "에스프레소",
                "price": "6,200원"
            },
            {
                "name": "카푸치노",
                "price": "6,500원"
            },
            {
                "name": "홍차",
                "price": "7,000원"
            },
            {
                "name": "에이드",
                "price": "7,500원"
            }
        ],
        "review": [
            {
                "user": "likeadaisy",
                "content": "분위기 좋고 적당히 시끄럽고 뷰는 너무 좋음",
                "date": "2021.06.12",
                "rating": "4"
            }
        ]
    },
    {
        "title": "신촌로스팅라이브러리",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20191030_75%2F15724388732505hOu9_JPEG%2F_RGK3DPCqnqOry46WhH2oFoS.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200209_49%2F1581232797883Dfgfv_JPEG%2FbHiShS_H8QDk5jtaleroDpi4.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200209_34%2F1581232271430cBJ1j_JPEG%2FZ1AdBkPzQ0zhogINJLvlzep6.jpg"
        ],
        "theme": "",
        "tel": "02-3145-1709",
        "address": "서울 서대문구 연세로 13 유플렉스 12층",
        "location": "신촌",
        "open": "매일 10:30 - 22:00",
        "insta": "http://www.instagram.com/roastinglibrary_sinchon",
        "convenience": "주차, 포장, 무선 인터넷, 남/녀 화장실 구분",
        "menu": [
            {
                "name": "아메리카노",
                "price": "5,400원"
            },
            {
                "name": "카페라떼",
                "price": "6,000원"
            },
            {
                "name": "플랫화이트",
                "price": "6,000원"
            },
            {
                "name": "카페모카",
                "price": "6,500원"
            }
        ],
        "review": [
            {
                "user": "로라",
                "content": "혼자 오기 좋아요 ㅎㅎ",
                "date": "2020.11.11",
                "rating": "5"
            }
        ]
    },
    {
        "title": "암흑카페",
        "img_url": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190808_203%2F1565262013687jIaqG_JPEG%2FAhYaE46SyCarKLXEK_QuEjnv.JPG.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20150901_9%2F1441069023549l6W25_JPEG%2F166681516432689_2.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20171129_17%2F1511922719734VGBVC_JPEG%2F5_.jpg"
        ],
        "theme": "편안한 분위기",
        "tel": "0507-1405-3760",
        "address": "서울 서대문구 연세로5길 26 준빌딩 8층",
        "location": "신촌",
        "open": "매일 11:30 - 23:00",
        "insta": "http://noongam.co.kr/",
        "convenience": "단체석, 주차, 예약, 남/녀 화장실 구분",
        "menu": [
            {
                "name": "평일체험",
                "price": "15,000원"
            },
            {
                "name": "주말체험",
                "price": "20,000원"
            },
            {
                "name": "식보 VR세트",
                "price": "30,000원"
            },
            {
                "name": "차보 VR세트",
                "price": "25,000원"
            }
        ],
        "review": [
            {
                "user": "ckqh",
                "content": "재미있어요",
                "date": "2021.06.11",
                "rating": "4"
            }
        ]
    }
]

for i in hongdae:
    db.cafes.insert_one({
        'title': i['title'],
        'img_url': i['img_url'],
        'theme': i['theme'],
        'tel': i['tel'],
        'address': i['address'],
        'location': i['location'],
        'open': i['open'],
        'convenience': i['convenience'],
        'instagram': i['insta'],
        'menu': i['menu'],
        'review': i['review']
    })
