# EuroScope 扇区简化生成工具
该项目目前未完成,请谨慎使用!

## 项目简介

EuroScope 扇区简化生成工具是一个用于生成 EuroScope 扇区简化文件的工具。它可以处理 VOR 和 NDB 数据，生成符合指定格式的 `.sct` 文件。该工具支持根据情报区生成文件或生成全部文件两种模式，并兼容底层扇区和 NAIP 数据版需求。

## 功能

- **按情报区生成**：将数据按照 `CODE_FIR` 分组，为每个情报区生成单独的 `.sct` 文件。
- **全部生成**：生成所有 VOR 和 NDB 数据的 `.sct` 文件。
- **数据格式转换**：从 CSV 文件读取数据并转换为 EuroScope 扇区文件格式。
- **支持 GBK 编码**：生成的 `.sct` 文件使用 GBK 编码保存，符合中文环境的要求。

## 安装

1. 克隆项目：
    ```bash
    git clone https://github.com/Yuziki1227/es_sector_tool.git
    cd es_sector_tool
    ```

2. 安装依赖（如果需要）：
    ```bash
    pip install -r requirements.txt
    ```

## 文件结构

- `Datafiles/`：存放原始数据版文件
- `generate/`：存放生成的 `.sct` 文件
- `require/`：包含工具脚本和文件处理逻辑
  - `csv_reader.py`：读取 CSV 文件的模块
  - `file_writer.py`：生成 `.sct` 文件的模块
- `README.md`：项目说明文件
- `main.py`：主脚本，处理不同的生成模式

## 使用方法

暂无,项目开发完毕后会补充

### 运行模式

该工具支持两种运行模式：

1. **按情报区生成**：
    ```bash
    python main.py --mode area
    ```
    该模式会根据情报区生成单独的 `.sct` 文件，存放在 `generate` 目录中。

2. **全部生成**：
    ```bash
    python main.py --mode all
    ```
    该模式会生成所有 VOR 和 NDB 数据的 `.sct` 文件，存放在 `generate` 目录中。

### 文件格式

- **VOR 文件格式**：
    ```
    [VOR]
    CODE_ID VAL_FREQ GEO_LAT GEO_LONG
    CODE_ID/TXT_NAME VAL_FREQ GEO_LAT GEO_LONG
    ```

- **NDB 文件格式**：
    ```
    [NDB]
    CODE_ID VAL_FREQ GEO_LAT GEO_LONG
    CODE_ID/TXT_NAME VAL_FREQ GEO_LAT GEO_LONG
    ```

### 坐标格式

坐标采用 `NDD.MM.SS.SSS` 和 `EDDD.MM.SS.SSS` 格式，其中：
- `N` 为北纬，`E` 为东经
- `DDD` 为度数，`MM` 为分钟，`SS.SSS` 为秒数

### 例子

- **输入数据**（VOR）：
    ```
    DGE 114.5 N11.45.14.000 E191.98.10.000
    DGE/果洛 114.5 N11.45.14.000 E191.98.10.000
    ```

- **输出文件**（VOR.sct）：
    ```
    [VOR]
    DGE 114.5 N11.45.14.000 E191.98.10.000
    DGE/果洛 114.5 N11.45.14.000 E191.98.10.000
    ```

## 开发和贡献

- 请遵循 [贡献指南](CONTRIBUTING.md) 进行贡献。
- 提交 Bug 报告和功能请求，请通过 [Issue Tracker](https://github.com/Yuziki1227/es_sector_tool/issues) 提交。

## 许可证

本项目采用 [私有许可证](LICENSE)，请务必参阅 `LICENSE` 文件。

## 联系信息

- **项目维护者**：Mingchun Chen
- **联系方式**：Yuziki1227@outlook.com