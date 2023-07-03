import basic_framework as bf


if __name__ == '__main__':
    bucharest_baf = bf.BasicAnalysisFramework()
    bucharest_baf.load_edgelist('../Data/Preprocessed/bucharest_edgelist.csv')
    bucharest_baf.compute_measurements()
    bucharest_baf.create_report().to_csv('../Data/Tables/basic/bucharest_basic_analysis.csv')
    print('Bucharest done.')

    china_baf = bf.BasicAnalysisFramework()
    china_baf.load_edgelist('../Data/Preprocessed/china_edgelist.csv')
    china_baf.compute_measurements()
    china_baf.create_report().to_csv('../Data/Tables/basic/china_basic_analysis.csv')
    print('China done.')

    hainan_baf = bf.BasicAnalysisFramework()
    hainan_baf.load_edgelist('../Data/Preprocessed/hainan_edgelist.csv')
    hainan_baf.compute_measurements()
    hainan_baf.create_report().to_csv('../Data/Tables/basic/hainan_basic_analysis.csv')
    print('Hainan done.')

    shanxi_baf = bf.BasicAnalysisFramework()
    shanxi_baf.load_edgelist('../Data/Preprocessed/shanxi_edgelist.csv')
    shanxi_baf.compute_measurements()
    shanxi_baf.create_report().to_csv('../Data/Tables/basic/shanxi_basic_analysis.csv')
    print('Shanxi done.')

    xian_baf = bf.BasicAnalysisFramework()
    xian_baf.load_edgelist('../Data/Preprocessed/xian_edgelist.csv')
    xian_baf.compute_measurements()
    xian_baf.create_report().to_csv('../Data/Tables/basic/xian_basic_analysis.csv')
    print('Xian done.')

    yunnan_baf = bf.BasicAnalysisFramework()
    yunnan_baf.load_edgelist('../Data/Preprocessed/yunnan_edgelist.csv')
    yunnan_baf.compute_measurements()
    yunnan_baf.create_report().to_csv('../Data/Tables/basic/yunnan_basic_analysis.csv')
    print('Yunnan done.')
