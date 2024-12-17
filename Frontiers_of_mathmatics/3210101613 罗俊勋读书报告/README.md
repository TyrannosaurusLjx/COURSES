# 文档结构

├── README.md <!-- here -->
├── 参考文件
│   └── THE MINIMAL DECEPTIVE PROBLEM REVISITED-  THE ROLE OF ``GENETIC WASTE''.pdf  <!-- 参考文献, 其余是网页链接, 还有一份无法下载 >
├── 读书报告
│   ├── README.md <!-- 读书报告的说明 -->
│   ├── assets <!-- 读书报告的图片等资源 -->
│   │   ├── font
│   │   │   └── Songti.ttc
│   │   └── img
│   │       ├── *.jpg
│   │       └── popnum_with_p00_0.7.jpg
│   ├── doc
│   │   ├── ZJU_Logo.pdf
│   │   ├── reference.bib <!-- 参考文献 -->
│   │   ├── report.cls
│   │   ├── report.pdf <!-- 读书报告的 PDF 版本 -->
│   │   └── report.tex
│   ├── report.pdf <!-- 读书报告的 PDF 版本 -->
│   └── src
│       ├── bestfitness_multi_sigle_mpoints.py <!-- 比较单点变异和多点变异的源代码 -->
│       ├── bestfitness_with_without_gw.py <!-- 比较有无 GW 的源代码 -->
│       ├── bestfitness_with_without_gw_and_scaling.py <!-- 比较有无 GW 和 GW scaling 的源代码 -->
│       ├── fitness_with_p00.py <!-- 绘制不同 p00 下的适应度函数的源代码 -->
│       ├── plot_fitness_function.py <!-- 绘制目标函数函数的源代码 -->
│       └── popnum_with_p00.py <!-- 绘制不同 p00 下的种群数量的源代码 -->
├── 读书报告 PPT.pdf <!-- 读书报告的 PDF 版本 -->
├── 参考文献----THE MINIMAL DECEPTIVE PROBLEM REVISITED-  THE ROLE OF ``GENETIC WASTE''.pdf <!-- 参考文献 -->
├── 读书报告.pdf <!-- 读书报告的 PDF 版本 -->
└── 读书报告展示 <!-- 读书报告的展示文件夹 -->
    ├── README.md
    ├── doc
    │   ├── img
    │   │   └── Figure_*.png
    │   ├── report.pdf
    │   ├── report.*
    │   ├── res
    │   │   └── **
    │   └── zju.sty
    ├── report.pdf
    └── src
        ├── __pycache__
        │   ├── GA.cpython-312.pyc
        │   ├── GA.cpython-313.pyc
        │   └── test_for_realnumber_coding.cpython-312.pyc
        ├── find_fmax.py
        ├── pm_fixed_and_dynamjc.py
        ├── pm_single_multi_gauss.py
        ├── test_for_binary_coding.py
        ├── test_for_population.py
        └── test_for_realnumber_coding.py