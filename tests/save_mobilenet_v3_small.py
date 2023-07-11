import torchvision
import torch
import numpy as np

# TODO: once #485 is fixed, we should save batchnorm eps and momentum
with torch.no_grad():
    model = torchvision.models.mobilenet_v3_small(weights='DEFAULT')
    model.eval()

    np.savez("mobilenet_v3_small.npz", **{
        # head
        "0.0.weight":       model.features[0][0].weight.numpy(),
        "0.1.scale":        model.features[0][1].weight.numpy(),
        "0.1.bias":         model.features[0][1].bias.numpy(),
        "0.1.running_mean": model.features[0][1].running_mean.numpy(),
        "0.1.running_var":  model.features[0][1].running_var.numpy(),

        # layer 1 (no expand, with SE)
        "1.0.0.0.weight":       model.features[1].block[0][0].weight.numpy(),
        "1.0.0.1.scale":        model.features[1].block[0][1].weight.numpy(),
        "1.0.0.1.bias":         model.features[1].block[0][1].bias.numpy(),
        "1.0.0.1.running_mean": model.features[1].block[0][1].running_mean.numpy(),
        "1.0.0.1.running_var":  model.features[1].block[0][1].running_var.numpy(),
        "1.0.1.fc1.weight":     model.features[1].block[1].fc1.weight.numpy(),
        "1.0.1.fc1_bias.bias":  model.features[1].block[1].fc1.bias.numpy(),
        "1.0.1.fc2.weight":     model.features[1].block[1].fc2.weight.numpy(),
        "1.0.1.fc2_bias.bias":  model.features[1].block[1].fc2.bias.numpy(),
        "1.0.2.0.weight":       model.features[1].block[2][0].weight.numpy(),
        "1.0.2.1.scale":        model.features[1].block[2][1].weight.numpy(),
        "1.0.2.1.bias":         model.features[1].block[2][1].bias.numpy(),
        "1.0.2.1.running_mean": model.features[1].block[2][1].running_mean.numpy(),
        "1.0.2.1.running_var":  model.features[1].block[2][1].running_var.numpy(),

        # layer 2
        "1.1.0.0.weight":       model.features[2].block[0][0].weight.numpy(),
        "1.1.0.1.scale":        model.features[2].block[0][1].weight.numpy(),
        "1.1.0.1.bias":         model.features[2].block[0][1].bias.numpy(),
        "1.1.0.1.running_mean": model.features[2].block[0][1].running_mean.numpy(),
        "1.1.0.1.running_var":  model.features[2].block[0][1].running_var.numpy(),
        "1.1.1.0.weight":       model.features[2].block[1][0].weight.numpy(),
        "1.1.1.1.scale":        model.features[2].block[1][1].weight.numpy(),
        "1.1.1.1.bias":         model.features[2].block[1][1].bias.numpy(),
        "1.1.1.1.running_mean": model.features[2].block[1][1].running_mean.numpy(),
        "1.1.1.1.running_var":  model.features[2].block[1][1].running_var.numpy(),
        "1.1.2.0.weight":       model.features[2].block[2][0].weight.numpy(),
        "1.1.2.1.scale":        model.features[2].block[2][1].weight.numpy(),
        "1.1.2.1.bias":         model.features[2].block[2][1].bias.numpy(),
        "1.1.2.1.running_mean": model.features[2].block[2][1].running_mean.numpy(),
        "1.1.2.1.running_var":  model.features[2].block[2][1].running_var.numpy(),

        # layer 3
        "1.2.0.0.0.weight":       model.features[3].block[0][0].weight.numpy(),
        "1.2.0.0.1.scale":        model.features[3].block[0][1].weight.numpy(),
        "1.2.0.0.1.bias":         model.features[3].block[0][1].bias.numpy(),
        "1.2.0.0.1.running_mean": model.features[3].block[0][1].running_mean.numpy(),
        "1.2.0.0.1.running_var":  model.features[3].block[0][1].running_var.numpy(),
        "1.2.0.1.0.weight":       model.features[3].block[1][0].weight.numpy(),
        "1.2.0.1.1.scale":        model.features[3].block[1][1].weight.numpy(),
        "1.2.0.1.1.bias":         model.features[3].block[1][1].bias.numpy(),
        "1.2.0.1.1.running_mean": model.features[3].block[1][1].running_mean.numpy(),
        "1.2.0.1.1.running_var":  model.features[3].block[1][1].running_var.numpy(),
        "1.2.0.1.1.epsilon":      model.features[3].block[1][1].eps,
        "1.2.0.1.1.momentum":     model.features[3].block[1][1].momentum,
        "1.2.0.2.0.weight":       model.features[3].block[2][0].weight.numpy(),
        "1.2.0.2.1.scale":        model.features[3].block[2][1].weight.numpy(),
        "1.2.0.2.1.bias":         model.features[3].block[2][1].bias.numpy(),
        "1.2.0.2.1.running_mean": model.features[3].block[2][1].running_mean.numpy(),
        "1.2.0.2.1.running_var":  model.features[3].block[2][1].running_var.numpy(),

        # layer 4 (with SE)
        "2.0.0.0.weight":       model.features[4].block[0][0].weight.numpy(),
        "2.0.0.1.scale":        model.features[4].block[0][1].weight.numpy(),
        "2.0.0.1.bias":         model.features[4].block[0][1].bias.numpy(),
        "2.0.0.1.running_mean": model.features[4].block[0][1].running_mean.numpy(),
        "2.0.0.1.running_var":  model.features[4].block[0][1].running_var.numpy(),
        "2.0.1.0.weight":       model.features[4].block[1][0].weight.numpy(),
        "2.0.1.1.scale":        model.features[4].block[1][1].weight.numpy(),
        "2.0.1.1.bias":         model.features[4].block[1][1].bias.numpy(),
        "2.0.1.1.running_mean": model.features[4].block[1][1].running_mean.numpy(),
        "2.0.1.1.running_var":  model.features[4].block[1][1].running_var.numpy(),
        "2.0.2.fc1.weight":     model.features[4].block[2].fc1.weight.numpy(),
        "2.0.2.fc1_bias.bias":  model.features[4].block[2].fc1.bias.numpy(),
        "2.0.2.fc2.weight":     model.features[4].block[2].fc2.weight.numpy(),
        "2.0.2.fc2_bias.bias":  model.features[4].block[2].fc2.bias.numpy(),
        "2.0.3.0.weight":       model.features[4].block[3][0].weight.numpy(),
        "2.0.3.1.scale":        model.features[4].block[3][1].weight.numpy(),
        "2.0.3.1.bias":         model.features[4].block[3][1].bias.numpy(),
        "2.0.3.1.running_mean": model.features[4].block[3][1].running_mean.numpy(),
        "2.0.3.1.running_var":  model.features[4].block[3][1].running_var.numpy(),

        # layer 5 (with SE)
        "2.1.0.0.0.weight":       model.features[5].block[0][0].weight.numpy(),
        "2.1.0.0.1.scale":        model.features[5].block[0][1].weight.numpy(),
        "2.1.0.0.1.bias":         model.features[5].block[0][1].bias.numpy(),
        "2.1.0.0.1.running_mean": model.features[5].block[0][1].running_mean.numpy(),
        "2.1.0.0.1.running_var":  model.features[5].block[0][1].running_var.numpy(),
        "2.1.0.1.0.weight":       model.features[5].block[1][0].weight.numpy(),
        "2.1.0.1.1.scale":        model.features[5].block[1][1].weight.numpy(),
        "2.1.0.1.1.bias":         model.features[5].block[1][1].bias.numpy(),
        "2.1.0.1.1.running_mean": model.features[5].block[1][1].running_mean.numpy(),
        "2.1.0.1.1.running_var":  model.features[5].block[1][1].running_var.numpy(),
        "2.1.0.2.fc1.weight":     model.features[5].block[2].fc1.weight.numpy(),
        "2.1.0.2.fc1_bias.bias":  model.features[5].block[2].fc1.bias.numpy(),
        "2.1.0.2.fc2.weight":     model.features[5].block[2].fc2.weight.numpy(),
        "2.1.0.2.fc2_bias.bias":  model.features[5].block[2].fc2.bias.numpy(),
        "2.1.0.3.0.weight":       model.features[5].block[3][0].weight.numpy(),
        "2.1.0.3.1.scale":        model.features[5].block[3][1].weight.numpy(),
        "2.1.0.3.1.bias":         model.features[5].block[3][1].bias.numpy(),
        "2.1.0.3.1.running_mean": model.features[5].block[3][1].running_mean.numpy(),
        "2.1.0.3.1.running_var":  model.features[5].block[3][1].running_var.numpy(),

        # layer 6 (with SE)
        "2.2.0.0.0.weight":       model.features[6].block[0][0].weight.numpy(),
        "2.2.0.0.1.scale":        model.features[6].block[0][1].weight.numpy(),
        "2.2.0.0.1.bias":         model.features[6].block[0][1].bias.numpy(),
        "2.2.0.0.1.running_mean": model.features[6].block[0][1].running_mean.numpy(),
        "2.2.0.0.1.running_var":  model.features[6].block[0][1].running_var.numpy(),
        "2.2.0.1.0.weight":       model.features[6].block[1][0].weight.numpy(),
        "2.2.0.1.1.scale":        model.features[6].block[1][1].weight.numpy(),
        "2.2.0.1.1.bias":         model.features[6].block[1][1].bias.numpy(),
        "2.2.0.1.1.running_mean": model.features[6].block[1][1].running_mean.numpy(),
        "2.2.0.1.1.running_var":  model.features[6].block[1][1].running_var.numpy(),
        "2.2.0.2.fc1.weight":     model.features[6].block[2].fc1.weight.numpy(),
        "2.2.0.2.fc1_bias.bias":  model.features[6].block[2].fc1.bias.numpy(),
        "2.2.0.2.fc2.weight":     model.features[6].block[2].fc2.weight.numpy(),
        "2.2.0.2.fc2_bias.bias":  model.features[6].block[2].fc2.bias.numpy(),
        "2.2.0.3.0.weight":       model.features[6].block[3][0].weight.numpy(),
        "2.2.0.3.1.scale":        model.features[6].block[3][1].weight.numpy(),
        "2.2.0.3.1.bias":         model.features[6].block[3][1].bias.numpy(),
        "2.2.0.3.1.running_mean": model.features[6].block[3][1].running_mean.numpy(),
        "2.2.0.3.1.running_var":  model.features[6].block[3][1].running_var.numpy(),

        # layer 7 (with SE)
        "3.0.0.0.weight":       model.features[7].block[0][0].weight.numpy(),
        "3.0.0.1.scale":        model.features[7].block[0][1].weight.numpy(),
        "3.0.0.1.bias":         model.features[7].block[0][1].bias.numpy(),
        "3.0.0.1.running_mean": model.features[7].block[0][1].running_mean.numpy(),
        "3.0.0.1.running_var":  model.features[7].block[0][1].running_var.numpy(),
        "3.0.1.0.weight":       model.features[7].block[1][0].weight.numpy(),
        "3.0.1.1.scale":        model.features[7].block[1][1].weight.numpy(),
        "3.0.1.1.bias":         model.features[7].block[1][1].bias.numpy(),
        "3.0.1.1.running_mean": model.features[7].block[1][1].running_mean.numpy(),
        "3.0.1.1.running_var":  model.features[7].block[1][1].running_var.numpy(),
        "3.0.2.fc1.weight":     model.features[7].block[2].fc1.weight.numpy(),
        "3.0.2.fc1_bias.bias":  model.features[7].block[2].fc1.bias.numpy(),
        "3.0.2.fc2.weight":     model.features[7].block[2].fc2.weight.numpy(),
        "3.0.2.fc2_bias.bias":  model.features[7].block[2].fc2.bias.numpy(),
        "3.0.3.0.weight":       model.features[7].block[3][0].weight.numpy(),
        "3.0.3.1.scale":        model.features[7].block[3][1].weight.numpy(),
        "3.0.3.1.bias":         model.features[7].block[3][1].bias.numpy(),
        "3.0.3.1.running_mean": model.features[7].block[3][1].running_mean.numpy(),
        "3.0.3.1.running_var":  model.features[7].block[3][1].running_var.numpy(),

        # layer 8 (with SE)
        "3.1.0.0.0.weight":       model.features[8].block[0][0].weight.numpy(),
        "3.1.0.0.1.scale":        model.features[8].block[0][1].weight.numpy(),
        "3.1.0.0.1.bias":         model.features[8].block[0][1].bias.numpy(),
        "3.1.0.0.1.running_mean": model.features[8].block[0][1].running_mean.numpy(),
        "3.1.0.0.1.running_var":  model.features[8].block[0][1].running_var.numpy(),
        "3.1.0.1.0.weight":       model.features[8].block[1][0].weight.numpy(),
        "3.1.0.1.1.scale":        model.features[8].block[1][1].weight.numpy(),
        "3.1.0.1.1.bias":         model.features[8].block[1][1].bias.numpy(),
        "3.1.0.1.1.running_mean": model.features[8].block[1][1].running_mean.numpy(),
        "3.1.0.1.1.running_var":  model.features[8].block[1][1].running_var.numpy(),
        "3.1.0.2.fc1.weight":     model.features[8].block[2].fc1.weight.numpy(),
        "3.1.0.2.fc1_bias.bias":  model.features[8].block[2].fc1.bias.numpy(),
        "3.1.0.2.fc2.weight":     model.features[8].block[2].fc2.weight.numpy(),
        "3.1.0.2.fc2_bias.bias":  model.features[8].block[2].fc2.bias.numpy(),
        "3.1.0.3.0.weight":       model.features[8].block[3][0].weight.numpy(),
        "3.1.0.3.1.scale":        model.features[8].block[3][1].weight.numpy(),
        "3.1.0.3.1.bias":         model.features[8].block[3][1].bias.numpy(),
        "3.1.0.3.1.running_mean": model.features[8].block[3][1].running_mean.numpy(),
        "3.1.0.3.1.running_var":  model.features[8].block[3][1].running_var.numpy(),

        # layer 9 (with SE)
        "4.0.0.0.weight":       model.features[9].block[0][0].weight.numpy(),
        "4.0.0.1.scale":        model.features[9].block[0][1].weight.numpy(),
        "4.0.0.1.bias":         model.features[9].block[0][1].bias.numpy(),
        "4.0.0.1.running_mean": model.features[9].block[0][1].running_mean.numpy(),
        "4.0.0.1.running_var":  model.features[9].block[0][1].running_var.numpy(),
        "4.0.1.0.weight":       model.features[9].block[1][0].weight.numpy(),
        "4.0.1.1.scale":        model.features[9].block[1][1].weight.numpy(),
        "4.0.1.1.bias":         model.features[9].block[1][1].bias.numpy(),
        "4.0.1.1.running_mean": model.features[9].block[1][1].running_mean.numpy(),
        "4.0.1.1.running_var":  model.features[9].block[1][1].running_var.numpy(),
        "4.0.2.fc1.weight":     model.features[9].block[2].fc1.weight.numpy(),
        "4.0.2.fc1_bias.bias":  model.features[9].block[2].fc1.bias.numpy(),
        "4.0.2.fc2.weight":     model.features[9].block[2].fc2.weight.numpy(),
        "4.0.2.fc2_bias.bias":  model.features[9].block[2].fc2.bias.numpy(),
        "4.0.3.0.weight":       model.features[9].block[3][0].weight.numpy(),
        "4.0.3.1.scale":        model.features[9].block[3][1].weight.numpy(),
        "4.0.3.1.bias":         model.features[9].block[3][1].bias.numpy(),
        "4.0.3.1.running_mean": model.features[9].block[3][1].running_mean.numpy(),
        "4.0.3.1.running_var":  model.features[9].block[3][1].running_var.numpy(),

        # layer 10 (with SE)
        "4.1.0.0.0.weight":       model.features[10].block[0][0].weight.numpy(),
        "4.1.0.0.1.scale":        model.features[10].block[0][1].weight.numpy(),
        "4.1.0.0.1.bias":         model.features[10].block[0][1].bias.numpy(),
        "4.1.0.0.1.running_mean": model.features[10].block[0][1].running_mean.numpy(),
        "4.1.0.0.1.running_var":  model.features[10].block[0][1].running_var.numpy(),
        "4.1.0.1.0.weight":       model.features[10].block[1][0].weight.numpy(),
        "4.1.0.1.1.scale":        model.features[10].block[1][1].weight.numpy(),
        "4.1.0.1.1.bias":         model.features[10].block[1][1].bias.numpy(),
        "4.1.0.1.1.running_mean": model.features[10].block[1][1].running_mean.numpy(),
        "4.1.0.1.1.running_var":  model.features[10].block[1][1].running_var.numpy(),
        "4.1.0.2.fc1.weight":     model.features[10].block[2].fc1.weight.numpy(),
        "4.1.0.2.fc1_bias.bias":  model.features[10].block[2].fc1.bias.numpy(),
        "4.1.0.2.fc2.weight":     model.features[10].block[2].fc2.weight.numpy(),
        "4.1.0.2.fc2_bias.bias":  model.features[10].block[2].fc2.bias.numpy(),
        "4.1.0.3.0.weight":       model.features[10].block[3][0].weight.numpy(),
        "4.1.0.3.1.scale":        model.features[10].block[3][1].weight.numpy(),
        "4.1.0.3.1.bias":         model.features[10].block[3][1].bias.numpy(),
        "4.1.0.3.1.running_mean": model.features[10].block[3][1].running_mean.numpy(),
        "4.1.0.3.1.running_var":  model.features[10].block[3][1].running_var.numpy(),

        # layer 11 (with SE)
        "4.2.0.0.0.weight":       model.features[11].block[0][0].weight.numpy(),
        "4.2.0.0.1.scale":        model.features[11].block[0][1].weight.numpy(),
        "4.2.0.0.1.bias":         model.features[11].block[0][1].bias.numpy(),
        "4.2.0.0.1.running_mean": model.features[11].block[0][1].running_mean.numpy(),
        "4.2.0.0.1.running_var":  model.features[11].block[0][1].running_var.numpy(),
        "4.2.0.1.0.weight":       model.features[11].block[1][0].weight.numpy(),
        "4.2.0.1.1.scale":        model.features[11].block[1][1].weight.numpy(),
        "4.2.0.1.1.bias":         model.features[11].block[1][1].bias.numpy(),
        "4.2.0.1.1.running_mean": model.features[11].block[1][1].running_mean.numpy(),
        "4.2.0.1.1.running_var":  model.features[11].block[1][1].running_var.numpy(),
        "4.2.0.2.fc1.weight":     model.features[11].block[2].fc1.weight.numpy(),
        "4.2.0.2.fc1_bias.bias":  model.features[11].block[2].fc1.bias.numpy(),
        "4.2.0.2.fc2.weight":     model.features[11].block[2].fc2.weight.numpy(),
        "4.2.0.2.fc2_bias.bias":  model.features[11].block[2].fc2.bias.numpy(),
        "4.2.0.3.0.weight":       model.features[11].block[3][0].weight.numpy(),
        "4.2.0.3.1.scale":        model.features[11].block[3][1].weight.numpy(),
        "4.2.0.3.1.bias":         model.features[11].block[3][1].bias.numpy(),
        "4.2.0.3.1.running_mean": model.features[11].block[3][1].running_mean.numpy(),
        "4.2.0.3.1.running_var":  model.features[11].block[3][1].running_var.numpy(),

        # tail
        "5.0.0.weight":       model.features[12][0].weight.numpy(),
        "5.0.1.scale":        model.features[12][1].weight.numpy(),
        "5.0.1.bias":         model.features[12][1].bias.numpy(),
        "5.0.1.running_mean": model.features[12][1].running_mean.numpy(),
        "5.0.1.running_var":  model.features[12][1].running_var.numpy(),
        "5.2.0.weight":       model.classifier[0].weight.numpy(),
        "5.2.0.bias":         model.classifier[0].bias.numpy(),
        "5.4.weight":         model.classifier[3].weight.numpy(),
        "5.4.bias":           model.classifier[3].bias.numpy(),
    })

    x = torch.randn(10, 3, 224, 224)
    np.save("mobilenet_v3_small_x.npy", x.numpy())

    y = model(x)
    np.save("mobilenet_v3_small_y.npy", y.numpy())
