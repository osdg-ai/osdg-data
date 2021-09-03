## Dataset Information

The *OSDG Community Dataset (OSDG-CD)* is the direct result of the work of hundreds of volunteers who have contributed to our understanding of [Sustainable Development Goals (SDGs)](https://sdgs.un.org/goals) via the [OSDG Community Platform (OSDG-CP)](https://osdg.ai/community). It contains thousands of text excerpts which were labelled by the community volunteers with respect to SDGs. For each piece of text, the suggested label was also validated by the [OSDG Labelling Tool (OSDG-LT)](https://github.com/osdg-ai/osdg-tool). The data can be used to derive insights into the nature of SDGs using either ontology-based or machine learning approaches. The OSDG-CP dataset will be updated on a quarterly basis.

## Methodology

The OSDG Community Platform is an ambitious attempt to bring together volunteers and subject matter experts from all around the world to create a large and accurate source of textual information on SDGs. It uses publicly available texts such as publications, reports and other written data sources. Each text is broken down into smaller pieces of paragraph length. These smaller pieces are then being labelled by the Community volunteers. Since the texts we collect have suggested labels associated with them – these usually come from the data source and do not necessarily reflect the content of a particular paragraph – each volunteer is presented with a single simple question that asks if the suggested label is indeed relevant for the short text at hand. Texts are labelled by multiple volunteers to ensure a high degree of quality.

## Documentation

The OSDG-CP dataset is currently provided in a `.csv` format in the `datasets` directory. It is a flat tabular dataset that contains the following columns:

- `text_id` - a unique text identifier.
- `doi` - DOI of the source text to which a given text excerpt belongs.
- `text` - the excerpt text itself.
- `sdg` - the suggested SDG label volunteers were asked to consider, i.e. accept/reject.
- `label_volunteers` - the final label derived from volunteer votes. `accepted` means that all volunteers accepted the suggested label while `rejected` denotes the text excerpts that were rejected by all volunteers. `undecided` means that there was a split vote among the volunteers.
- `label_osdg` - the indicator of whether or not the suggested SDG label was also among the labels assigned to the text by OSDG-LT. `accepted` is only assigned if the suggested label was assigned by OSDG-LT with *Strong relevance*.

## Relevant Papers

Pukelis, Lukas, et al. ‘OSDG -- Open-Source Approach to Classify Text Data by UN Sustainable Development Goals (SDGs)’. ArXiv:2005.14569 [Cs], May 2020. arXiv.org, http://arxiv.org/abs/2005.14569.

## Usage Examples

Examples of text classification using OSDG-CD can be found under the `examples` directory:
- `osdg-cd-example-classifier-sklearn.ipynb` ([open in nbviewer](https://nbviewer.jupyter.org/github/osdg-ai/osdg-data/blob/main/examples/osdg-cd-example-classifier-sklearn.ipynb))

## Share Your Work

The *OSDG Community Dataset (OSDG-CD)* is made available for research purposes. We are making this data open with the hope to enable researchers to discover new insights into and meaningful connections among Sustainable Development Goals.

We would like to know what you discover in the data. So do not hesitate to share with us your outputs, be it a research paper, a machine learning model, a blog post, or just an interesting observation. Send us an email at [community@osdg.ai](mailto:community@osdg.ai?subject=OSDG-CP). If you are using the dataset in a research paper, you can attribute the dataset as *OSDG Community Dataset v2021.07*.

## Contribute to OSDG

This datasets is made possible because of a large community effort. We would be glad to see your contribution to the project too. You can join our
[Community Platform](https://osdg.ai/community) to help us collect more labelled data. If you have a more technical background, you can also contribute to the OSDG Labelling Tool [here](https://github.com/osdg-ai/osdg-tool). If you want to contribute to the project in some other way, do let us know via this [contact form](https://osdg.ai/contact).

To learn more about the OSDG project, visit [osdg.ai](https://osdg.ai/about).

## FAQ

TBA.
