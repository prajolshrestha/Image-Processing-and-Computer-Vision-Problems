% Intensity-based Image Segmentation

% learn: meshgrid, conv2, contour, bwlabeln

%% 
N = 400;

% create 2D Gaussian for Smoothing
tmpvec = zscore(1:round(N/4));
[X,Y] = meshgrid(tmpvec);
gaus2d = exp(-(X.^2 + Y.^2));

% create image and convert to z-values
img = conv2(randn(N,N),gaus2d,'same');
zimg = (img-mean(img(:))) / std(img(:));

%% pick std threshold
zthresh = 2;

%binarize the thresholded image (one-tailed!)
[bimap,numclust] = bwlabeln( zimg > zthresh);


figure(1),clf
subplot(131)
contourf(zimg,40)
axis square
set(gca,'xtick',[],'ytick',[])
colorbar
title('Original Image')


subplot(132)
imagesc(bimap)
axis square
title('Binarized image')
set(gca,'xtick',[],'ytick',[])
axis xy

subplot(133),hold on
contourf(zimg,40)
contour(logical(bimap),2,'k','LineWidth',2)
axis square
set(gca,'xtick',[],'ytick',[])
title('Contour Outlining')


