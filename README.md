# Lyrics_Encoding_Fix

Fixes unreadable music lyrics file due to encoding
Chinese lyrics - Effective
Korean lyrics - Limited

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
