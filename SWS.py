import torch
import torch.nn as nn


class SimAMWithSlicing(nn.Module):
    def __init__(self, e_lambda=1e-4):
        super(SimAMWithSlicing, self).__init__()
        self.activation = nn.Sigmoid()
        self.e_lambda = e_lambda

    def forward(self, x):
        batch_size, num_channels, height, width = x.size()

        block_size_h = height // 2
        block_size_w = width // 2


        block1 = x[:, :, :block_size_h, :block_size_w]
        block2 = x[:, :, :block_size_h, block_size_w:]
        block3 = x[:, :, block_size_h:, :block_size_w]
        block4 = x[:, :, block_size_h:, block_size_w:]

        enhanced_blocks = []
        for block in [block1, block2, block3, block4]:
            n = block_size_h * block_size_w - 1
            block_minus_mu_square = (block - block.mean(dim=[2, 3], keepdim=True)).pow(2)
            y = block_minus_mu_square / (
                        4 * (block_minus_mu_square.sum(dim=[2, 3], keepdim=True) / n + self.e_lambda)) + 0.5
            enhanced_blocks.append(block * self.activaton(y))

        enhanced_image = torch.cat([torch.cat([enhanced_blocks[0], enhanced_blocks[1]], dim=3),
                                    torch.cat([enhanced_blocks[2], enhanced_blocks[3]], dim=3)], dim=2)

        return enhanced_image


if __name__ == '__main__':
    input = torch.randn(1, 1024, 7, 7)  
    model = SimAMWithSlicing()
    outputs = model(input)
