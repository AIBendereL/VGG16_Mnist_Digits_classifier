import torch

from torchvision.models import vgg16, VGG16_Weights



if __name__ == "__main__":
    MODEL_WEIGHTS_PATH = "vgg16_weights.pth"
    weights = VGG16_Weights.IMAGENET1K_V1
    
    model = vgg16(weights = weights)
    
    torch.save(model.state_dict(), MODEL_WEIGHTS_PATH)