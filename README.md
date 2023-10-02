## Dataset Information

The **OSDG Community Dataset (OSDG-CD)** is the direct result of the work of hundreds of volunteers who have contributed to our understanding of [Sustainable Development Goals (SDGs)](https://sdgs.un.org/goals) via the [OSDG Community Platform (OSDG-CP)](https://osdg.ai/community). It contains thousands of text excerpts which were labelled by the community volunteers with respect to SDGs. The data can be used to derive insights into the nature of SDGs using either ontology-based or machine learning approaches. The OSDG Community Dataset will be updated on a quarterly basis.

Please note that all versions of the dataset are hosted on **Zenodo**. This repository is only intended to provide examples of how the dataset can be used in practice. You can access different versions of the dataset using DOI handles above. The **Most Recent** handle **always resolves to the latest version**.

| Version | DOI Handle |
| --- | --- |
| Most Recent | <a href="https://doi.org/10.5281/zenodo.5550237"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.5550237.svg" alt="DOI"></a> |
| Version 2023.10 | <a href="https://doi.org/10.5281/zenodo.7540165"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.8397907.svg" alt="DOI"></a> |
| Version 2023.07 | <a href="https://doi.org/10.5281/zenodo.7540165"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.8107038.svg" alt="DOI"></a> |
| Version 2023.04 | <a href="https://doi.org/10.5281/zenodo.7540165"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.7816403.svg" alt="DOI"></a> |
| Version 2023.01 | <a href="https://doi.org/10.5281/zenodo.7540165"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.7540165.svg" alt="DOI"></a> |
| Version 2022.10 | <a href="https://doi.org/10.5281/zenodo.7136826"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.7136826.svg" alt="DOI"></a> |
| Version 2022.07 | <a href="https://doi.org/10.5281/zenodo.6831287"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.6831287.svg" alt="DOI"></a> |
| Version 2022.04 | <a href="https://doi.org/10.5281/zenodo.6393942"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.6393942.svg" alt="DOI"></a> |
| Version 2022.01 | <a href="https://doi.org/10.5281/zenodo.5792547"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.5792547.svg" alt="DOI"></a> |
| Version 2021.09 | <a href="https://doi.org/10.5281/zenodo.5550238"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.5550238.svg" alt="DOI"></a> |

## Methodology

The OSDG Community Platform is an ambitious attempt to bring together volunteers and subject matter experts from all around the world to create a large and accurate source of textual information on SDGs. It uses publicly available texts such as publications, reports and other written data sources. Each text is broken down into smaller pieces of paragraph length. These smaller pieces are then being labelled by the Community volunteers. Since the texts we collect have suggested labels associated with them – these usually come from the data source and do not necessarily reflect the content of a particular paragraph – each volunteer is presented with a single simple question that asks if the suggested label is indeed relevant for the short text at hand. Texts are labelled by multiple volunteers to ensure a high degree of quality.

## Documentation

The OSDG-CD dataset is provided in a `.csv` format on Zenodo. It is a flat tabular dataset that contains the following columns:

- `doi` - Digital Object Identifier of the original document;
- `text_id` - unique text identifier;
- `text` - text excerpt from the document;
- `sdg` - the SDG the text is validated against;
- `labels_negative` - the number of volunteers who rejected the suggested SDG label;
- `labels_positive` - the number of volunteers who accepted the suggested SDG label;
- `agreement` - agreement score based on the formula $\text{agreement} = \frac{|labels_{positive} - labels_{negative}|}{labels_{positive} + labels_{negative}}$;

## Relevant Papers

Pukelis, L., Bautista-Puig, N., Statulevičiūtė, G., Stančiauskas, V., Dikmener, G., &amp; Akylbekova, D. (2022, November 21). OSDG 2.0: A multilingual tool for classifying text data by UN Sustainable Development Goals (SDGs). arXiv.org. https://doi.org/10.48550/arXiv.2211.11252 

Pukelis, L., Puig, N. B., Skrynik, M., &amp; Stanciauskas, V. (2020, May 29). OSDG -- Open-source approach to classify text data by UN Sustainable Development Goals (sdgs). arXiv.org. https://arxiv.org/abs/2005.14569 

## Usage Examples

Examples of text classification using OSDG-CD can be found under the `examples` directory:
- `osdg-cd-example-classifier-sklearn.ipynb` ([open in nbviewer](https://nbviewer.jupyter.org/github/osdg-ai/osdg-data/blob/main/examples/osdg-cd-example-classifier-sklearn.ipynb))

## Share Your Work

The OSDG Community Dataset (OSDG-CD) is made available for research purposes. We are making the data open with the hope to enable researchers to discover new insights into and meaningful connections among Sustainable Development Goals.

We would like to know what you discover in the data. So do not hesitate to share with us your outputs, be it a research paper, a machine learning model, a blog post, or just an interesting observation. Send us an email at [community@osdg.ai](mailto:community@osdg.ai?subject=OSDG-CD).

If you are using the dataset in a research paper, please cite the original version as follows:

> OSDG, UNDP IICPSD SDG AI Lab, & PPMI. (2021). OSDG Community Dataset (OSDG-CD) (2021.09) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.5550238.

To cite a specific version, use the template provided on Zenodo. 

## Contribute to OSDG

This dataset is made possible because of a large community effort. We would be glad to see your contribution to the project too. You can join our [Community Platform](https://osdg.ai/community) to help us collect more labelled data. If you have a more technical background, you can also contribute to the OSDG Labelling Tool [here](https://github.com/osdg-ai/osdg-tool). If you want to contribute to the project in some other way, do let us know via this [contact form](https://osdg.ai/contact).

To learn more about the OSDG project, visit [osdg.ai](https://osdg.ai/about).
