from autogen.autogen_images import mint

with open("seeds.txt", "r") as f:
    # seeds = [int(line[:-1]) for line in f]
    seeds = [int(line) for line in f]

out_path = "files/images"
for seed in seeds:
    try:
        mint(seed=seed, out_path=out_path)
    except ValueError as e:
        print(seed, e)
        continue
