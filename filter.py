import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import matplotlib.pyplot as mp

PATH = r'C:\Users\xulingfeng\Desktop\python学习\数学分析\DS\data\noised.wav'
PATH_OUT = r'C:\Users\xulingfeng\Desktop\python学习\数学分析\DS\data\filter.wav'

# 时域
sample_rate, noised_sigs = wf.read(PATH)   # 返回采样频率和信号强度，返回的是十六进制
noised_sigs = noised_sigs / 2**15
times = np.arange(len(noised_sigs)) / sample_rate

# 频域
freqs = nf.fftfreq(times.size, d=1/sample_rate)
noised_ffts = nf.fft(noised_sigs)
noised_pows = np.abs(noised_ffts)

# 滤波
fund_freq = freqs[noised_pows.argmax()]        # 查找最大值所在频率的坐标
# print(fund_freq)
noised_indices = np.where(np.abs(freqs) != fund_freq)       # 去除非基频的下标
filter_ffts = noised_ffts.copy()
filter_ffts[noised_indices] = 0
filter_pows = np.abs(filter_ffts)

# 滤波结果映射回时间域
filter_sigs = nf.ifft(filter_ffts).real

# 写回文件
wf.write(PATH_OUT, sample_rate, (filter_sigs * 2 ** 15).astype(np.int16))

mp.figure('Filter', facecolor='lightgray')
mp.subplot(221)
mp.title('Time Domain', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:178], noised_sigs[:178], c='orangered', label='Noise')
mp.legend()

mp.subplot(222)
mp.title('Freq Domain', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.semilogy(freqs[freqs>=0], noised_pows[freqs>=0], c='dodgerblue', label='Noise')  # 使用半对数坐标，纵轴使用对数坐标
mp.legend()

mp.subplot(223)
mp.title('Time Domain', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:178], filter_sigs[:178], c='hotpink', label='Filter')
mp.legend()

mp.subplot(224)
mp.title('Freq Domain', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.semilogy(freqs[freqs>=0], filter_pows[freqs>=0], c='limegreen', label='Filter')  # 使用半对数坐标，纵轴使用对数坐标
mp.legend()

mp.tight_layout()
mp.show()

# print(noised_sigs)