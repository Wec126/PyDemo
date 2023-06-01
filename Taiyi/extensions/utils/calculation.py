import torch
import torch.linalg as linalg


def cal_cov_matrix(input):
    return torch.cov(input.T)


def cal_eig(input):
    eigvals= linalg.eigvals(input)
    return eigvals




if __name__ == '__main__':
    # test cal_cov_matrix
    x = torch.randn((1, 10))
    print(x.shape)
    y = cal_cov_matrix(x)
    print(y.shape)

    # test cal_eig
    # x = torch.randn((10, 10))
    # y = cal_eig(x)
    # print(y)
    # print(y.size())