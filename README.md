## Empathetic Response Generation via Reinforcement Learning with Empathy Alignment and Semantic Relevance
This is the official implementation for paper Empathetic Response Generation via Reinforcement Learning with Empathy Level Alignment and Semantic Relevance

## Setup
- Install the required libraries

```console
pip install -r requirements.txt
```
The project mainly referenced the code from [EmpRL](https://github.com/butterfliesss/EmpRL). If there are issues during installation, try using the environments provided by this project.

## Dataset
- Download the preprocessed datasets from [here](https://drive.google.com/drive/folders/16JPd75eSylpB9G6HKFf89aoG7wZipJTf?usp=drive_link), and put them into `data/`.
- Download the trained empathy identifiers from [here](https://drive.google.com/drive/folders/1FEA9KoW1rf2Sfz9swHWmECqvcZyuidbo?usp=drive_link), and put them into `saved/`.

## Run RLES
- Generator Fine-tuning:
```console
bash run_dialog.sh
```
- RL Training:
```console
bash run_dialog_ppo.sh
```
- Response Generation:
```console
bash run_dialog_eval.sh
```

For reproducibility, we place the model checkpoints at [checkpoint](https://drive.google.com/drive/folders/1HxKWSS0ovyb4VmgOyV5RbPfCtnJAGsHl?usp=sharing). 
Download and place it in a folder, then pass that folder’s path to the `run_dialog_eval.sh` script and run it.

