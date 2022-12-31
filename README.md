# Lyrics_Encoding_Fix

Fixes unreadable music lyrics file
- English lyrics - Effective
- Chinese lyrics - Effective
- Japanese lyrics - Effective
- Korean lyrics - Limited

## Example Usage

### fix("雨爱.lrc")

#### Original File (雨爱.lrc)
```
[ti:�갮]
[ar:��ة��]
[al:Rainie & Love��? �갮]
[by:]
[offset:0]
[00:00.00]�갮 - ��ة�� (Rainie Yang)
[00:03.32]�ʣ�Wonderful
[00:06.65]���������
[00:09.98]������������
[00:13.31]�����ˣ�Ѧ����
[00:16.64]���������
[00:21.12]������ ����ı���
[00:26.76]������ �����ҿ���
[00:33.10]������ ��Ҳ���뿴��
[00:38.78]�뿪�� �Ұ����ĳ���
[00:42.45]���̽����ľ���
[00:45.44]�ҵ�����������
[00:48.44]ѧ�����
[00:51.45]��������� һ�ε�����
[00:54.50]��ĺ�������������ҵİ���
[00:59.78]��ϣ�������²�ͣ
[01:03.40]��������� �ð���͸��
[01:09.56]�Ұ��ϸ��������� Rainie love
[01:15.29]�������� һ�ε��ۻ�
[01:18.48]���ڵ�ʪ���񴢴氮��ļ���
[01:23.92]��ϣ�������²�ͣ
[01:27.44]�갮������ ��һֱ����
[01:33.56]�������ҽ��ῴ��
[01:36.87]�ʺ������
[02:04.66]����Ŀ���
[02:09.13]����Ϣ ���޷�����
[02:14.80]һ��� ��εľ���
[02:21.17]�ܳ��� �ð���ʧ��Ϣ
[02:26.80]�뿪�� �Ұ����ĳ���
[02:30.45]���̽����ľ���
[02:33.47]�ҵ�����������
[02:36.39]ѧ�����
[02:42.38]��������� һ�ε�����
[02:45.47]��ĺ�������������ҵİ���
[02:50.76]��ϣ�������²�ͣ
[02:54.51]��������� �ð���͸��
[03:00.53]�Ұ��ϸ��������� Rainie love
[03:06.39]�������� һ�ε��ۻ�
[03:09.47]���ڵ�ʪ���񴢴氮��ļ���
[03:14.87]��ϣ�������²�ͣ
[03:18.44]�갮��������һֱ����
[03:24.52]�������ҽ��ῴ��
[03:27.83]�ʺ������
[03:33.61]���ڵ�ʪ���񴢴氮��ļ���
[03:38.84]��ϣ�������²�ͣ
[03:42.43]�갮��������һֱ����
[03:48.58]�������ҽ��ῴ��
[03:51.81]�ʺ������
```

#### Fixed File (fixed_雨爱.lrc)
```
[ti:雨爱]
[ar:杨丞琳]
[al:Rainie & Love…? 雨爱]
[by:]
[offset:0]
[00:00.00]雨爱 - 杨丞琳 (Rainie Yang)
[00:03.32]词：Wonderful
[00:06.65]曲：金大洲
[00:09.98]编曲：黄宣铭
[00:13.31]制作人：薛忠铭
[00:16.64]窗外的天气
[00:21.12]就像是 你多变的表情
[00:26.76]下雨了 雨陪我哭泣
[00:33.10]看不清 我也不想看清
[00:38.78]离开你 我安静的抽离
[00:42.45]不忍揭晓的剧情
[00:45.44]我的泪流在心里
[00:48.44]学会放弃
[00:51.45]听雨的声音 一滴滴清晰
[00:54.50]你的呼吸像雨滴渗入我的爱里
[00:59.78]真希望雨能下不停
[01:03.40]让想念继续 让爱变透明
[01:09.56]我爱上给我勇气的 Rainie love
[01:15.29]窗外的雨滴 一滴滴累积
[01:18.48]屋内的湿气像储存爱你的记忆
[01:23.92]真希望雨能下不停
[01:27.44]雨爱的秘密 能一直延续
[01:33.56]我相信我将会看到
[01:36.87]彩虹的美丽
[02:04.66]冷冷的空气
[02:09.13]很窒息 我无法呼吸
[02:14.80]一万颗 雨滴的距离
[02:21.17]很彻底 让爱消失无息
[02:26.80]离开你 我安静的抽离
[02:30.45]不忍揭晓的剧情
[02:33.47]我的泪流在心里
[02:36.39]学会放弃
[02:42.38]听雨的声音 一滴滴清晰
[02:45.47]你的呼吸像雨滴渗入我的爱里
[02:50.76]真希望雨能下不停
[02:54.51]让想念继续 让爱变透明
[03:00.53]我爱上给我勇气的 Rainie love
[03:06.39]窗外的雨滴 一滴滴累积
[03:09.47]屋内的湿气像储存爱你的记忆
[03:14.87]真希望雨能下不停
[03:18.44]雨爱的秘密能一直延续
[03:24.52]我相信我将会看到
[03:27.83]彩虹的美丽
[03:33.61]屋内的湿气像储存爱你的记忆
[03:38.84]真希望雨能下不停
[03:42.43]雨爱的秘密能一直延续
[03:48.58]我相信我将会看到
[03:51.81]彩虹的美丽
```

### fix("さよならくちびる.lrc")

#### Original File (さよならくちびる.lrc)
```
[ti:����ʤ餯���Ӥ� (���ټ����촽����Ӱ������)]
[ar:�ϥ�쥪 (haruleo)]
[al:����ʤ餯���Ӥ�]
[by:]
[offset:0]
[kana:1111111111��1�Ϥ�1���1�Ҥ�1���礯1�Ϥ�1���1�Ҥ�1����1����1���礦1���礦1�Ĥ�1��1��1�֤�1��1���夦1����1��1�Ӥ礦1��1�錄��1����1��1��1��1�Ȥ�1��1�魯1�錄��1����1����1�狼1��1����1��1�錄��1����1����1����1��1�Ϥ�1����1����1����1��1����1��1�Ĥ�1����1����1����1����1�Ȥ�1����1��1����1������1����1�Ϥ�1����1��1����1��1�դ�1��1�֤�1���1����1��1���礦1����1����1�䤵1����1�ޤ�1��1�錄��1����1����1�錄��1����1����1�狼1��1����1��1�錄��1����1�錄��1�狼1��]
[00:00.00]����ʤ餯���Ӥ� (���ټ����촽����Ӱ������) - �ϥ�쥪 (haruleo)
[00:00.00]�ʣ��ػ���
[00:00.00]�����ػ���
[00:01.51]���¤��ϕN��
[00:07.38]����äƤ���ݤ�����
[00:12.62]Ŀ�w���_����Τ��P������
[00:19.39]�������˽����
[00:25.48]���줬������Ȥ狼�ä�
[00:30.70]�o������ �դ���Ȥ�
[00:33.42]�ۤۤ����
[00:37.07]���μ��ϒi���ʤ��ޤޤǤ���
[00:43.41]���ä�����ʤ��Ǥ��뤫��
[00:50.13]����ʤ餯���Ӥ�
[00:52.96]˽�Ͻ��l�˄e���椲���
[00:58.93]����Ҋ�Ĥ�ʤ���
[01:02.07]����ʤ餯���Ӥ�
[01:04.92]˽�� �� �Ϥ����
[01:07.93]�����ˤ���ʹ�ߤ��ۤ���֪�ä���
[01:21.00]��ɫ����ڤ������T�Ꝣ���Ƥ�
[01:32.19]�������r�䤫��ӳ����
[01:38.55]���θ�Ϥɤ��ؤ�줫�ʤ�
[01:44.84]���äȿդ������Ƥ�������
[01:51.70]����ʤ餯���Ӥ�
[01:54.42]����Ǥ�ޤ�����
[01:57.48]�Ĥ��Ф֤��x�줿���ʤ����
[02:03.57]����ʤ餯���Ӥ�
[02:06.48]���դ줽�������~��ŤƤ�
[02:10.89]���Ф��˻��Ĥ�������
[02:19.85]�Է֤��������ؤͤƤ��ޤ�����
[02:31.88]�������ϤϤ⤦��������
[02:42.68]�Ĥ᤿�������Ӥ�
[02:45.47]���Ͻ�ʤ�ƃ�����
[02:49.90]�������۲�򤷤Ƥ��
[02:54.65]�ۤɤ��뤯���Ӥ�
[02:57.52]˽�ϤǤ�_���˾Ȥ��Ƥ����
[03:06.55]����ʤ餯���Ӥ�
[03:09.44]˽�Ͻ��l�˄e���椲���
[03:15.44]����Ҋ�Ĥ�ʤ���
[03:18.51]����ʤ餯���Ӥ�
[03:21.40]˽�Ͻ�˽�˄e���椲���
[03:27.29]���꤬�Ȥ�����ʤ�
```

#### Fixed File (fixed_さよならくちびる.lrc)
```
[ti:さよならくちびる (《再见，嘴唇》电影主题曲)]
[ar:ハルレオ (haruleo)]
[al:さよならくちびる]
[by:]
[offset:0]
[kana:1111111111し1はた1もと1ひろ1きょく1はた1もと1ひろ1たい1おん1じょう1しょう1つた1き1ま1ぶた1あ1ちゅう1ちょ1に1びょう1ご1わたし1さい1ご1む1り1とげ1ぬ1わす1わたし1いま1だれ1わか1つ1きみ1み1わたし1いま1いた1あい1し1はい1いろ1こう1かい1せ1かい1ぬ1つぶ1きみ1あざ1うつ1うた1とど1そら1き1きみ1こころ1さけ1はな1こと1ば1あわ1ひ1ふさ1じ1ぶん1よわ1かさ1い1じょう1きみ1いま1やさ1かな1まな1ざ1わたし1たし1すく1わたし1いま1だれ1わか1つ1きみ1み1わたし1いま1わたし1わか1つ]
[00:00.00]さよならくちびる (《再见，嘴唇》电影主题曲) - ハルレオ (haruleo)
[00:00.00]词：秦基博
[00:00.00]曲：秦基博
[00:01.51]体温の上昇が
[00:07.38]伝わっている気がして
[00:12.62]目蓋を開けるのを躊躇した
[00:19.39]二秒後の私たち
[00:25.48]これが最後だとわかって
[00:30.70]無理して ふたりとも
[00:33.42]ほほえんだ
[00:37.07]この棘は抜けないままでいい
[00:43.41]ずっと忘れないでいるから
[00:50.13]さよならくちびる
[00:52.96]私は今誰に別れを告げるの
[00:58.93]君を見つめながら
[01:02.07]さよならくちびる
[01:04.92]私は 今 はじめて
[01:07.93]ここにある痛みが愛だと知ったよ
[01:21.00]灰色の後悔が世界を塗り潰しても
[01:32.19]君だけ鮮やかに映るんだ
[01:38.55]この歌はどこへも届かない
[01:44.84]きっと空に消えていくだけ
[01:51.70]さよならくちびる
[01:54.42]それでもまだ君に
[01:57.48]心が叫ぶの離れたくないよと
[02:03.57]さよならくちびる
[02:06.48]あふれそうな言葉を慌てて
[02:10.89]たばこに火をつけ塞いだ
[02:19.85]自分の弱さを重ねてごまかして
[02:31.88]これ以上はもうダメだよね
[02:42.68]つめたいくちびる
[02:45.47]君は今なんて優しく
[02:49.90]悲しい眼差しをしてるの
[02:54.65]ほどけるくちびる
[02:57.52]私はでも確かに救われてたんだ
[03:06.55]さよならくちびる
[03:09.44]私は今誰に別れを告げるの
[03:15.44]君を見つめながら
[03:18.51]さよならくちびる
[03:21.40]私は今私に別れを告げるよ
[03:27.29]ありがとうさよな
```

### fix("さよならくちびる.lrc")

#### Original File (さよならくちびる.lrc)
```
[ti:SCIENTIST]
[ar:TWICE (&#53944;&#50752;&#51060;&#49828;)]
[al:Formula of Love: O+T=<3]
[by:]
[offset:0]
[00:01.06]SCIENTIST - TWICE (&#53944;&#50752;&#51060;&#49828;)
[00:01.77]�ʣ�&#51648;&#10;&#91;
[00:02.10]����anne marie/melanie fontana/michel "lindgren" schulz/tommy brown/steven franks/72
[00:04.27]������tommy brown/mr. franks/michel "lindgren" schulz
[00:05.69]Original publisher��jyp publishing (komca)/emi music publishing ltd/universal music publishing group/sony music publishing/champagne therapy/reservoir media music/the key artist publishing
[00:05.77]Sub-publisher��jyp publishing (komca)/universal music publishing group/sony music publishing/universal music publishing group/reservoir media management/inc./the key artist agency
[00:05.85]Sessions vocal productions by��lindgren
[00:05.87]Background vocals by��melanie fontana/sophia pae
[00:05.89]Vocals directed by��&#49;&#93;&#68;
[00:05.91]Digital editing by��&#93;&#82;&#101;
[00:05.92]Recorded by��&#101;&#32;&#115;/&#117;&#100;&#105; at jype studios
[00:05.94]Mixed by��&#100;&#105;&#111; at jype studios
[00:05.96]Mastered by��&#32;&#109;&#97; at 821 sound mastering
[00:05.99]&#55; &#51;&#49; &#50500; &#49800;&#53440;&#51064;
[00:07.31]&#57;&#46;&#52;&#57;&#93;&#10; &#48;&#48;&#58;
[00:09.49]
[00:10.19]&#49; &#53;&#49;&#93; &#105;&#110; &#99;
[00:11.51]Sin cos&#48128; &#32;&#45817;&#44592;
[00:14.23]&#55;&#50; &#45236;&#32;&#49828; &#51068;
[00:15.72]&#58; &#56;&#46;&#51;&#54; &#50508; &#48372;&#45796;&#32;
[00:18.36]&#46;&#57;&#54;&#93; &#50640; &#48159;&#55176;
[00:19.96]&#48;&#48; &#50;&#50;&#46;&#50; &#93; &#32; &#44033;&#51060;
[00:22.20]&#91; &#48;&#58;&#50; &#46;&#54; &#93;&#47672;&#47551; &#47564;&#32;
[00:27.60]&#48;&#48;&#58;&#51; &#46;&#54;&#48;&#93;&#10; &#48; &#58;
[00:30.60]
[00:31.76]&#91; &#48; &#51;&#53;&#46; &#56; &#66; &#116;&#116;&#101;
[00:35.88]Better make a move
[00:38.70]Love ain't a science
[00:40.46]Don't need no license
[00:42.33]&#117;&#115; &#91;&#48;&#48; &#52;&#54;&#46;&#54;&#49; minus
[00:46.61]Don't try to be a genius
[00:48.86]Why so serious
[00:50.84]&#48;&#48; &#53;&#51; &#49;&#55; wooah
[00:53.17]&#119;&#104; &#116;&#32; &#32;&#119; what u what u waiting for
[00:56.39]
[00:56.96]&#46;&#51; &#93; &#46041;&#50504;&#32;&#45208;
[00:58.32]&#46;&#53;&#48; &#10;&#91; &#49;&#58;
[01:00.50]
[01:01.09]&#46;&#52; &#93;&#83;&#111; &#119;&#104;
[01:02.45]So what's the next class then
[01:04.71]
[01:05.42]&#102;&#97; &#108;&#117;&#114;&#101;&#10; &#48;&#49; &#48;&#57;&#46; failure
[01:09.29]&#49; &#46;&#48;&#48; &#45236;&#32;&#47576;&#51008;&#32;
[01:11.00]&#49; &#46;&#51; &#93; &#32;&#49373;&#44033;&#51060;
[01:13.38]&#91; &#49;&#58;&#49; &#46;&#52; &#93;&#47672;&#47551; &#47564;&#32;
[01:18.47]&#48;&#49;&#58;&#50; &#46;&#54;&#48;&#93;&#10; &#48; &#58;
[01:21.60]
[01:22.63]&#91; &#49; &#50;&#54;&#46; &#52; &#10; &#48;&#49;&#58;
[01:26.54]
[01:27.07]Better make a move
[01:29.52]Love ain't a science
[01:31.25]Don't need no license
[01:33.25]&#117;&#115; &#91;&#48;&#49; &#51;&#55;&#46;&#53;&#48; minus
[01:37.50]Don't try to be a genius
[01:39.81]Why so serious
[01:41.38]
[01:41.94]&#48;&#49; &#52;&#52; &#49;&#52; wooah
[01:44.14]&#119;&#104; &#116;&#32; &#32;&#119; what u what u waiting for
[01:47.35]
[01:48.18]You got a crush on me
[01:49.07]
[01:50.06]You're gonna fall for me
[01:51.23]
[01:51.88]&#10;&#91; &#49;&#58;&#53; &#46;&#48;&#51; &#73;&#116; &#115;&#32;
[01:54.03]It's all useless uh-huh
[01:55.84]&#49800;&#53440; &#10;&#91;&#48; genius &#48372;&#45800;&#32;&#48520;&#46020;
[01:57.76]&#46993;&#52996; &#53440;&#51064;&#10; curious &#93;&#52376;&#47100;&#32;&#46028;&#51652;
[01:59.86]&#48;&#50; &#48;&#50;&#46; &#52;&#93;&#44144; &#50630;&#51060;&#32;
[02:02.04]&#58;&#48;&#50;&#46; &#57;&#93; rush
[02:02.99]Got a crush on me
[02:04.51]&#32;&#47792; &#10;&#91; &#50;&#58;&#48;&#56; &#54; &#93; &#51012; &#47792;&#46972;
[02:08.62]&#32;&#47792; &#10;&#91; &#50;&#58;&#49;&#50; &#56; &#93; &#49324; &#54616;&#45208;
[02:12.85]&#51088;&#10; &#48;&#50; &#49;&#55; &#48;&#51;&#93; &#32;&#54616;&#45208;&#47564;
[02:17.03]&#47100; &#91;&#48;&#50; &#50;&#48; &#54;&#55; &#76; &#118;&#101;&#32;
[02:20.67]Love ain't a science uhm-uhm
[02:22.72]Need no license uhm-uhm
[02:24.84]&#117;&#116;&#32; about me 'bout me
[02:26.66]&#117;&#116;&#32; you know 'bout me
[02:28.96]Love ain't a science uhm-uhm
[02:31.11]Need no license uhm-uhm
[02:33.24]&#32;&#117;&#32;&#119; what u what u what u waiting for
[02:37.66]Love ain't a science
[02:39.21]Don't need no license
[02:41.20]&#117;&#115; &#91;&#48;&#50; &#52;&#53;&#46;&#52;&#49; minus
[02:45.41]Don't try to be a genius
[02:47.85]Why so serious
[02:49.93]&#48;&#50; &#53;&#50; &#48;&#54; wooah
[02:52.06]&#119;&#104; &#116;&#32; &#32;&#119; what u what u waiting for
[02:55.41]
[03:03.19]Better move
[03:03.98]
[03:04.68]What u waiting
[03:06.45]What u waiting
```

#### Fixed File (fixed_さよならくちびる.lrc)
```
[ti:SCIENTIST]
[ar:TWICE (트와이스)]
[al:Formula of Love: O+T=<3]
[by:]
[offset:0]
[00:01.06]SCIENTIST - TWICE (트와이스)
[00:01.77]锟绞ｏ拷지[
[00:02.10]锟斤拷锟斤拷anne marie/melanie fontana/michel "lindgren" schulz/tommy brown/steven franks/72
[00:04.27]锟斤拷锟斤拷锟斤拷tommy brown/mr. franks/michel "lindgren" schulz
[00:05.69]Original publisher锟斤拷jyp publishing (komca)/emi music publishing ltd/universal music publishing group/sony music publishing/champagne therapy/reservoir media music/the key artist publishing
[00:05.77]Sub-publisher锟斤拷jyp publishing (komca)/universal music publishing group/sony music publishing/universal music publishing group/reservoir media management/inc./the key artist agency
[00:05.85]Sessions vocal productions by锟斤拷lindgren
[00:05.87]Background vocals by锟斤拷melanie fontana/sophia pae
[00:05.89]Vocals directed by锟斤拷1]D
[00:05.91]Digital editing by锟斤拷]Re
[00:05.92]Recorded by锟斤拷e s/udi at jype studios
[00:05.94]Mixed by锟斤拷dio at jype studios
[00:05.96]Mastered by锟斤拷 ma at 821 sound mastering
[00:05.99]7 31 아 슈타인
[00:07.31]9.49] 00:
[00:09.49]
[00:10.19]1 51] in c
[00:11.51]Sin cos밀  당기
[00:14.23]72 내 스 일
[00:15.72]: 8.36 알 보다 
[00:18.36].96] 에 밟히
[00:19.96]00 22.2 ]   각이
[00:22.20][ 0:2 .6 ]머릿 만 
[00:27.60]00:3 .60] 0 :
[00:30.60]
[00:31.76][ 0 35. 8 B tte
[00:35.88]Better make a move
[00:38.70]Love ain't a science
[00:40.46]Don't need no license
[00:42.33]us [00 46.61 minus
[00:46.61]Don't try to be a genius
[00:48.86]Why so serious
[00:50.84]00 53 17 wooah
[00:53.17]wh t   w what u what u waiting for
[00:56.39]
[00:56.96].3 ] 동안 나
[00:58.32].50 [ 1:
[01:00.50]
[01:01.09].4 ]So wh
[01:02.45]So what's the next class then
[01:04.71]
[01:05.42]fa lure 01 09. failure
[01:09.29]1 .00 내 맘은 
[01:11.00]1 .3 ]  생각이
[01:13.38][ 1:1 .4 ]머릿 만 
[01:18.47]01:2 .60] 0 :
[01:21.60]
[01:22.63][ 1 26. 4  01:
[01:26.54]
[01:27.07]Better make a move
[01:29.52]Love ain't a science
[01:31.25]Don't need no license
[01:33.25]us [01 37.50 minus
[01:37.50]Don't try to be a genius
[01:39.81]Why so serious
[01:41.38]
[01:41.94]01 44 14 wooah
[01:44.14]wh t   w what u what u waiting for
[01:47.35]
[01:48.18]You got a crush on me
[01:49.07]
[01:50.06]You're gonna fall for me
[01:51.23]
[01:51.88][ 1:5 .03 It s 
[01:54.03]It's all useless uh-huh
[01:55.84]슈타 [0 genius 보단 불도
[01:57.76]랑켄 타인 curious ]처럼 돌진
[01:59.86]02 02. 4]거 없이 
[02:02.04]:02. 9] rush
[02:02.99]Got a crush on me
[02:04.51] 몰 [ 2:08 6 ] 을 몰라
[02:08.62] 몰 [ 2:12 8 ] 사 하나
[02:12.85]자 02 17 03]  하나만
[02:17.03]럼 [02 20 67 L ve 
[02:20.67]Love ain't a science uhm-uhm
[02:22.72]Need no license uhm-uhm
[02:24.84]ut  about me 'bout me
[02:26.66]ut  you know 'bout me
[02:28.96]Love ain't a science uhm-uhm
[02:31.11]Need no license uhm-uhm
[02:33.24] u w what u what u what u waiting for
[02:37.66]Love ain't a science
[02:39.21]Don't need no license
[02:41.20]us [02 45.41 minus
[02:45.41]Don't try to be a genius
[02:47.85]Why so serious
[02:49.93]02 52 06 wooah
[02:52.06]wh t   w what u what u waiting for
[02:55.41]
[03:03.19]Better move
[03:03.98]
[03:04.68]What u waiting
[03:06.45]What u waiting
```
